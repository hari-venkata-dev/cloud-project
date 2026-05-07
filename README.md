# Cloud App – Docker, Kubernetes & CI/CD

This project is a simple cloud-native application that I built to better understand how applications move from local development into a containerized and Kubernetes-based environment.

The goal was not just to get an app running, but to go through the full deployment flow — build → containerize → deploy → expose → automate — while also learning how to troubleshoot real issues along the way.

---

## Architecture

User → Flask App → Docker Container → Kubernetes Deployment → Kubernetes Service

---

## What this project does

This is a lightweight Flask application with a few basic endpoints:

- `/`
  Returns:
  ```text
  Cloud App Running!