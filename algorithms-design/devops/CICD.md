

<details>
<summary> CI/CD  </summary>

* User commits code: A developer writes some code and commits it to GitHub.

* GitHub webhook triggers Jenkins: GitHub sends a webhook to Jenkins to notify it that there's new code to build.

* Jenkins builds the code: Jenkins pulls the code from GitHub, builds it, runs tests, and packages it up.

* Jenkins pushes the artifact to GCP: Assuming the build is successful, Jenkins pushes the artifact (e.g., a Docker image) to a GCP registry.
  * In Jenkins, create a deployment pipeline that includes the following steps:
  * Build the Docker image and push it to the Google Container Registry
  * Use the Kubernetes command-line tool (kubectl) to apply the deployment and service YAML files to the appropriate namespace in GKE. You can pass in variables to customize the deployment for each environment.
* Configure your deployment pipeline to trigger automatically when changes are pushed to your Git repository.

* GCP deploys the artifact: GCP pulls the artifact from the registry and deploys it to a development environment.

</details>