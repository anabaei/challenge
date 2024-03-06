<details>
    <summary> What is Microservice </summary>

* Microservices is a software architected design which includes small, independent services. couple loosely
  * Service is an abstraction of set of pods and one service policy to define how to access pods (k8 service yaml file define it)
  * 
* The main idea behind microservices is to break down large monolithic applications into smaller, independently deployable services that can be developed and managed by small, autonomous teams. 
* This approach allows teams to work more efficiently, innovate faster, and scale their applications more easily, since each service can be scaled independently based on its own specific needs.
* To ensure that the services are loosely coupled and can be developed and deployed independently,  best practices, of design principles are:
  * Single Responsibility Principle (SRP): Each service should have a single responsibility, and should be focused on providing a specific business capability.
  * Autonomous teams: Each service should be owned and managed by a small, autonomous team that has end-to-end responsibility for the service.
  * Service contracts: Services should communicate with each other using well-defined, versioned APIs that are agreed upon through service contracts.
  * Decentralized data management: Each service should have its own data store, and should be responsible for managing its own data.
  * Resilience and fault tolerance: Services should be designed to be resilient and fault-tolerant, so that they can continue to operate even if other services fail.

</details>
<details>
    <summary> API GateWays </summary>

* Usually uses for routing and checking authentication from requests
  * If request not having `Bearer token` then send send `401` 
  * If have `bearer token` validate it using `jwt` decode to check expiray and valid public key.  
</details>
<details>
    <summary> Deploy Microservice to GKE </summary>

* Create GKE in GCP
* Create and image of microservice and push to GCR
* Define microservice deployment yaml file for each microservice
  * Replicas, ports, label them (use label in service to be called), naming

* Define Kubernetes service
  * creates virtual IP address that the clients can use to access the service & balance traffic to different instances

```bash

```
</details>
<details>
    <summary> Deployment yaml file </summary>

* Define microservice deployment yaml file for each microservice
  * It will manage the lifecycle of your microservices for each you assign the image, give a name, replicas numbers, open port
* Deploy microservice deployment `kind` to GKE using kubectl
```bash
kubectl -f deploymicroservice.yaml 
```
</details>

<details>
    <summary> Kubernetes Service  yaml file </summary>

* Define Kubernetes service to balance traffic to instances
  *  it automatically creates an endpoint for the service, which is a virtual IP address that the clients can use to access the service.
  * By default, Kubernetes services in GKE use a round-robin load balancing algorithm
  * Kubernetes services are not local load balancers, but they do provide a way to load balance traffic to the different instances of a microservice
  * If you want to expose a microservice, need to define stable endpoint, to allow client hit the endpoints
  * K8 services are not LB, but they load balance traffic to different instances of microservice. 
  * When you create K8 services, it creates automatically a static endpoint which is a virtual IP address that the clients can use to access the service, it is called cluster IP address
  * If you need to handle more complex traffic management scenarios, such as routing traffic based on URL path or header values, or splitting traffic between different versions of a microservice, you can use Kubernetes ingress controllers or external load balancers in combination with Kubernetes services

* lable: my-app
* expose port 80
* forward traffic to port 8080 on the selected pod
* type lb means it balance traffic
```bash
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 8080
  type: LoadBalancer
```
#### Steps to deploy
* Save yaml file locally
* make sure kubectl installed locally
```bash
# run this command to create the service in your GKE cluster
kubectl apply -f my-kubernetes-service.yaml
# To verify that the service is created
kubectl get services
# to find what static ip 
# service-name is the name of kubernetes service
kubectl get services <service-name> -o jsonpath='{.spec.clusterIP}'
```

### Make DNS IP address 

*  while Kubernetes services provide internal cluster communication, Ingress is essential for managing external access to your application services and adding advanced routing features
  
*  Kubernetes services provide a way to expose your application endpoints within the cluster, allowing other parts of your application to discover and communicate with those endpoints. However, services alone cannot expose your application to the internet or external network.

* The IP provided in the K8 service could be use by DNS
  * first assign it at global
  * Then put it into k8 service
```bash
# to reserve your static ip address you can use
gcloud compute addresses create my-ip-address --global
```
* then added as ip address in k8 service
```bash
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: LoadBalancer
  loadBalancerIP: <your-static-ip-address>
```

</details>
<details>
    <summary>  Jason Web Token  </summary>

* A private key use to create token encode
* A public key use to verify the token validation, decode
* The client sends a request to the server, including a JWT token in the request header.
* The server receives the request and extracts the JWT token.
* The server then verifies the token by checking the digital signature.
* To check the digital signature, the server uses the public key that corresponds to the private key that was used to sign the token.
* If the digital signature is valid, the server can trust that the token was not tampered with and can proceed with processing the request.
* If the digital signature is not valid, the server rejects the token and returns an error response.
* To sign and verify JWT tokens, you can use a library that supports JWT, such as the jsonwebtoken library for Node.js. Here is an example of how to sign and verify a JWT token using jsonwebtoken:
```javascript
const jwt = require('jsonwebtoken');
// Sign a JWT token using a private key
const payload = { user_id: 123 };
const privateKey = 'my_private_key';
const token = jwt.sign(payload, privateKey);

// Verify the JWT token using a public key
const publicKey = 'my_public_key';
jwt.verify(token, publicKey, (err, decoded) => {
  if (err) {
    console.error('Invalid token:', err);
  } else {
    console.log('Decoded token:', decoded);
  }
});
```
</details>
<details>
    <summary> IP Address expose to Internet  ingress and controller</summary>

* Ingress is a Kubernetes resource that provides a way to manage external HTTP/HTTPS access to the services in k8 cluster. Ingress acts as a load balancer,reverse proxy, routing incoming traffic to the appropriate service based on the request's URL path and other rules defined in the Ingress configuration
* `Ingress Controllers` is a component responsible for ingress rules, can be cofigured to work as load balancer to distribute traffic to multiple pods running the same service 
* NGINX is one `Ingress Controllers`. Can be configured to validate JWT token using jwt_token module. The jwt includes a public key which 
* In addition to providing external access to your services, Ingress also allows you to configure advanced routing rules, SSL/TLS termination, and other features that are not available with a standard Kubernetes service. For example, you can use Ingress to route traffic to different services based on the domain name, or to add authentication and authorization policies for incoming requests.
* 

</details>
<details>
    <summary> LB in GKE </summary>

* On top of the k8 service which uses round robin algorithm to distribute traffic between instances/pods of service, we can distribute traffic on different regions and data centers. This allows you to provide a highly available and low-latency service to your users.
  
* `Google Cloud Load Balancing`: GKE can integrate with Google Cloud Load Balancing to distribute traffic to your Kubernetes services across multiple regions and data centers. 
* `External Load Balancers`: You can also configure GKE to use Network Load Balancer, to balance traffic across multiple data centers or regions

</details>
<details>
    <summary> </summary>

</details>

