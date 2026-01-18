# devsecops-runtime-security
This project demonstrates a DevSecOps-oriented Kubernetes deployment where a vulnerable Flask application is monitored for runtime security threats using Falco and performance metrics using Prometheus and Grafana. It showcases real-time detection of abnormal container behavior such as unauthorized shell access and sensitive file access.
# End-to-End DevSecOps Project  
## Secure Application Lifecycle with Docker and Kubernetes, Falco, Semgrep, Trivy & Prometheus

---

## 1. Introduction

This project demonstrates a **complete DevSecOps lifecycle** using a deliberately vulnerable Flask application.  
Security is implemented at **every stage** of the software lifecycle:

- Code level (SAST)
- Secrets detection
- Container image scanning
- Kubernetes deployment
- Runtime threat detection
- Monitoring and observability

The goal is to **shift security left and right**, ensuring applications are secure **before and during runtime**.

---

## 2. Why This Project?

Modern cloud-native applications face threats at multiple levels:
- Vulnerable source code
- Hardcoded secrets
- Insecure container images
- Runtime attacks inside containers

This project shows **how DevSecOps solves these problems** using open-source tools widely used in industry.

---

## 3. Project Objectives

- Build a vulnerable Flask web application
- Detect vulnerabilities using static analysis
- Identify exposed secrets
- Scan container images for CVEs
- Deploy application on Kubernetes
- Detect abnormal runtime behavior using Falco
- Monitor cluster health using Prometheus & Grafana

---

## 4. Project Architecture

### Architecture Explanation

- **Developer Layer**  
  The developer writes application code containing intentional vulnerabilities for learning purposes.

- **Security Shift-Left Layer**  
  - *Semgrep* scans source code for insecure patterns.
  - *TruffleHog* checks for exposed secrets before deployment.

- **Container Security Layer**  
  - Docker packages the application.
  - Trivy scans the container image for known vulnerabilities (CVEs).

- **Kubernetes Runtime Layer**  
  - Application is deployed on Minikube.
  - Falco monitors runtime behavior using system call analysis.
  - Prometheus collects performance and health metrics.
  - Grafana visualizes metrics and alerts.

This architecture ensures **end-to-end security visibility** across the DevSecOps pipeline.

---

## Tools and Technologies

| Category | Tool / Technology | Purpose |
|--------|------------------|--------|
| Programming Language | Python | Application development |
| Web Framework | Flask | Web application |
| Virtual Environment | Python venv | Dependency isolation |
| Containerization | Docker | Package application |
| Static Code Analysis | Semgrep | Detect code vulnerabilities |
| Secrets Scanning | TruffleHog | Detect exposed secrets |
| Image Security | Trivy | Container vulnerability scanning |
| Container Orchestration | Kubernetes (Minikube) | Deploy and manage containers |
| Package Manager | Helm | Kubernetes application deployment |
| Runtime Security | Falco | Detect abnormal runtime behavior |
| Monitoring | Prometheus | Metrics collection |
| Visualization | Grafana | Dashboards and alerts |
| Version Control | Git | Source code management |
| Platform | GitHub | Code hosting and CI/CD |

---

