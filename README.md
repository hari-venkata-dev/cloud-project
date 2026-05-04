# Cloud App – Docker, Kubernetes & CI/CD

This project is a simple cloud-native application that I built to practice how an application moves from local development to a containerized and Kubernetes-based setup.

The goal was not just to run an app, but to understand the full flow — build → containerize → deploy → expose → automate.

---

## What this project does

It’s a small Flask application with a single endpoint:

* `/` → returns **"Cloud App Running!"**

I used this simple app as a base to focus more on infrastructure and deployment rather than application complexity.

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
4. Exposed it using a service
5. Added a CI pipeline to automate build checks

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

Apply the config:

```bash
kubectl apply -f deployment.yaml
```

Check pods:

```bash
kubectl get pods
```

Since this is running locally, I used port-forward:

```bash
kubectl port-forward service/cloud-service 5000:5000
```

Then access:

```
http://localhost:5000
```

---

## CI/CD

I added a GitHub Actions workflow that:

* Runs on every push to main
* Installs dependencies
* Does a basic app check
* Builds the Docker image

---

## Issues I ran into (and fixed)

This was actually the most useful part of the project:

* **Docker not running properly**
  → Fixed by starting Docker Desktop correctly

* **Kubernetes not connecting**
  → Had to enable Kubernetes and wait for cluster to be ready

* **Image not found (ErrImageNeverPull)**
  → Fixed by adjusting image tag and pull policy

* **NodePort not working on localhost**
  → Used `kubectl port-forward` instead

---

## What I learned

* How Docker images are built and used
* How Kubernetes manages pods and deployments
* Difference between local vs cluster image access
* How services expose applications
* Basic CI/CD setup using GitHub Actions

---

## Next improvements

If I extend this project further, I would:

* Split into microservices (Go + Python)
* Add monitoring (Prometheus/Grafana)
* Deploy to AWS (EKS)
* Use Terraform for infrastructure

---

## Summary

This project helped me understand the full lifecycle of deploying a cloud-native application, including real debugging scenarios that come up when working with Docker and Kubernetes.
