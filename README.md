# 🚀 Cloud-Native Application with Docker, Kubernetes & CI/CD

This project demonstrates an end-to-end cloud-native application built using Python, containerized with Docker, deployed on Kubernetes, and automated using a CI/CD pipeline.

---

## 📌 Overview

The goal of this project is to simulate a real-world cloud deployment workflow:

* Build a backend service
* Containerize using Docker
* Deploy to Kubernetes
* Expose the application via a service
* Automate builds using CI/CD

---

## 🏗 Architecture

User → Flask App → Docker Container → Kubernetes Deployment → Kubernetes Service

---

## 🛠 Tech Stack

* **Programming Language:** Python (Flask)
* **Containerization:** Docker
* **Orchestration:** Kubernetes
* **CI/CD:** GitHub Actions
* **Version Control:** Git & GitHub

---

## ⚙️ Application Details

* Flask-based web application
* Endpoint:

  ```
  /
  ```
* Response:

  ```
  Cloud App Running!
  ```

---

## ▶️ Run Locally (Without Docker)

```bash
pip install -r requirements.txt
python app.py
```

Access:

```
http://localhost:5000
```

---

## 🐳 Run with Docker

### Build Docker image

```bash
docker build -t cloud-app:latest .
```

### Run container

```bash
docker run -p 5000:5000 cloud-app:latest
```

Access:

```
http://localhost:5000
```

---

## ☸️ Kubernetes Deployment

### Apply deployment and service

```bash
kubectl apply -f deployment.yaml
```

### Check pods

```bash
kubectl get pods
```

### Port forward (for local access)

```bash
kubectl port-forward service/cloud-service 5000:5000
```

Access:

```
http://localhost:5000
```

---

## 🔄 CI/CD Pipeline

GitHub Actions pipeline is configured to:

* Trigger on every push to `main`
* Install dependencies
* Validate application startup
* Build Docker image

Workflow file:

```
.github/workflows/ci.yml
```

---

## 🧠 Key Learnings

* Built and deployed a containerized application
* Understood Docker image lifecycle
* Deployed workloads in Kubernetes
* Debugged real-world issues like:

  * Image pull failures
  * Pod restarts
  * Service exposure
* Implemented CI/CD pipeline for automation

---

## ⚠️ Challenges & Fixes

### Kubernetes Image Pull Issue

* **Problem:** `ErrImageNeverPull`
* **Fix:** Used correct image tag and `imagePullPolicy`

### Service Not Accessible

* **Problem:** NodePort not accessible on localhost
* **Fix:** Used `kubectl port-forward`

### Docker Daemon Issues

* Ensured Docker Desktop was running correctly

---

## 📌 Future Improvements

* Add microservices (Go + Python)
* Integrate monitoring (Prometheus & Grafana)
* Deploy on AWS (EKS)
* Add Terraform for Infrastructure as Code
* Implement authentication service

---

## 🙌 Conclusion

This project demonstrates a complete DevOps workflow from development to deployment, including containerization, orchestration, and automation.
