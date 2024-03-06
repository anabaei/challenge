
# nginx
* Nginx is a web server software that can also be used as a reverse proxy, load balancer, and HTTP cache. It is designed to handle high traffic websites and is known for its speed, reliability, and scalability.
* To have nginx as LB in GKE:
  * 1- Create Deployment Yaml file as:
    *  kind: deployment
    *  name: nginx-deployment
    *  replicas: 3
    *  image: nginx:latest
    *  containerPort: 80
  * 2- Create nginx service to expose nginx-deployment as LB service 
    * kind: service
    * name: nginx-service
    * port: 80
    * targetport: 80
    * type: LoadBalancer

  * 3-  Use K8 command to run Nginx deployment and service To GKE 
```bash
kubectl apply -f nginx-deployment.yaml
kubectl apply -f nginx-service.yaml
```
  * 4-  Access the Nginx lb using the external IP address of the load balancer service. You can find the external IP address using the following command
```bash
kubectl get service nginx-service
```
  * 5- appropriate firewall roles set up to the upcoming requests to the LB

# istio 
![1_vpEtDrqeNQHoMw3WTKAQiA](https://user-images.githubusercontent.com/7471619/225780788-f1e09242-a085-490f-a261-5c06c3568dd6.jpg)

* istio is a mesh platform that provides advanced traffic management, observability, and security for microservices-based applications. It enables the developers to configure and control traffic flow, implement security policies, and gain visibility into their services. 
* Istio runs as a separate layer on top of the Kubernetes cluster and provides an abstracted interface to manage the service-to-service communication.
* To run it you need to install it on GKE
```bash
curl -L https://istio.io/downloadIstio | sh -
# to verify it is installed on GKE
kubectl get pods -n istio-system
```
* 1- create deployement a service into k8
```bash
# hello is out service name
kubectl create deployment hello --image=gcr.io/google-samples/hello-app:1.0
```
* 2- create service istio including gateway and service  yaml file
  * apiVersion: networking.isto.io/v1
  * kind: gateway
  * name: hello-world-gateway
  * istio: ingeresgateway
  * port: 80
    * name: http
    * protocul: HTTP
  * host: *
* 3- create istio service
  * apiVersion: networking.isto.io/v1
  * kind: VirtualService
  * name: hello-world-virtualservice
  * istio: ingeresgateway
  * route:
    * host: hello
  * port: 80
# grpc

# forward proxy

