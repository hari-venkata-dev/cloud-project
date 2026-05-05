# Cloud App – Docker, Kubernetes & CI/CD

This project is a simple cloud-native application that I built to understand how an application moves from local development to a containerized and Kubernetes-based setup.

The focus was not just on running an app, but on going through the full flow — build → containerize → deploy → expose → automate — and dealing with real issues along the way.

---

## Architecture

User → Flask App → Docker Container → Kubernetes Deployment → Kubernetes Service

---

## What this project does

It’s a small Flask application with two endpoints:

* `/` → returns **"Cloud App Running!"**
* `/health` → returns service status (used for Kubernetes health checks)

I intentionally kept the application simple so I could focus more on infrastructure, deployment, and debugging.

---

## Tech stack used

* Python (Flask)
* Docker
* Kubernetes (Docker Desktop)
* GitHub Actions (CI/CD)

---

## How I approached this

I built this step by step:

1. Created a simple Flask app
2. Containerized it using Docker
3. Deployed it into a Kubernetes cluster
4. Exposed it using a Service
5. Added a CI pipeline to automate build checks
6. Added liveness and readiness probes for better Kubernetes health management

---

## Running the app locally

```bash
pip install -r requirements.txt
python app.py
```

Then open:

```
http://localhost:5000
```

---

## Running with Docker

Build the image:

```bash
docker build -t cloud-app:latest .
```

Run the container:

```bash
docker run -p 5000:5000 cloud-app:latest
```

Open:

```
http://localhost:5000
```

---

## Kubernetes deployment

The application is deployed using a Kubernetes Deployment and exposed via a Service.

Apply the config:

```bash
kubectl apply -f deployment.yaml
```

Check pods:

```bash
kubectl get pods
```

Since this is running locally, I used port-forward to access it:

```bash
kubectl port-forward service/cloud-service 5000:5000
```

Then open:

```
http://localhost:5000
```

---

## CI/CD

I added a GitHub Actions workflow that:

* Runs on every push to `main`
* Installs dependencies
* Performs a basic application validation
* Builds the Docker image

---

## Issues I ran into (and fixed)

This was actually the most useful part of the project:

* **Docker not running properly**
  → Fixed by starting Docker Desktop correctly

* **Kubernetes not connecting**
  → Enabled Kubernetes and waited for the cluster to be ready

* **Image not found (ErrImageNeverPull)**
  → Fixed by adjusting image tag and image pull policy

* **Service not accessible via NodePort**
  → Used `kubectl port-forward` for local access

---

## What I learned

* How Docker images are built and optimized
* How Kubernetes manages deployments and pods
* How health checks (liveness/readiness probes) work
* Difference between local images and cluster image access
* How services expose applications
* Basic CI/CD setup using GitHub Actions
* How to debug real-world deployment issues

---

## Next improvements

If I extend this project further, I would:

* Split into microservices (Go + Python)
* Add monitoring (Prometheus/Grafana)
* Deploy on AWS (EKS)
* Use Terraform for infrastructure
* Add authentication layer

---

## Summary

This project helped me understand the full lifecycle of deploying a cloud-native application, including real debugging scenarios that come up when working with Docker and Kubernetes. It also gave me a better understanding of how different components fit together in a production-like setup.
