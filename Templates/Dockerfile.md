# 🐳 Dockerfile Template

**File Type:** Dockerfile  
**Author:**  
**Date:**  
**Version:**  

---

## 📚 Overview
A Dockerfile is a text document containing instructions to build a Docker image automatically.  
Each line in a Dockerfile represents a step that forms part of the final image layer stack.  
This template outlines common directives, best practices, and usage examples.

---

## 🧠 Key Concepts
| Concept | Description | Example |
|----------|--------------|----------|
| Image | Blueprint for containers | `FROM ubuntu:22.04` |
| Container | Running instance of an image | `docker run myimage` |
| Layer | Each command adds a layer | `RUN apt update` |
| Build Context | Directory sent to Docker daemon | `docker build .` |
| Tag | Version label for image | `myimage:latest` |

---

## 🧩 Basic Dockerfile Structure
    # Base image
    FROM python:3.11-slim

    # Maintainer info
    LABEL maintainer="you@example.com"
    LABEL version="1.0"
    LABEL description="Example Python Application Container"

    # Set working directory
    WORKDIR /app

    # Copy project files
    COPY . /app

    # Install dependencies
    RUN pip install --no-cache-dir -r requirements.txt

    # Expose port
    EXPOSE 5000

    # Command to run on container start
    CMD ["python", "main.py"]

---

## ⚙️ Common Directives
| Directive | Description | Example |
|------------|-------------|----------|
| `FROM` | Base image to start from | `FROM alpine:latest` |
| `LABEL` | Metadata about the image | `LABEL author="Josh"` |
| `WORKDIR` | Sets the working directory | `WORKDIR /usr/src/app` |
| `COPY` | Copies files from host | `COPY . /app` |
| `ADD` | Like COPY but can extract archives | `ADD app.tar.gz /app` |
| `RUN` | Executes command in a new layer | `RUN apt-get update && apt-get install -y curl` |
| `ENV` | Sets environment variables | `ENV PORT=8080` |
| `EXPOSE` | Documents network ports | `EXPOSE 8080` |
| `CMD` | Default command for container | `CMD ["node", "server.js"]` |
| `ENTRYPOINT` | Fixed main command | `ENTRYPOINT ["python3"]` |
| `ARG` | Defines build-time variables | `ARG VERSION=latest` |
| `VOLUME` | Mount point for persistence | `VOLUME /data` |

---

## 🧰 Example: Node.js Application
    FROM node:20-alpine

    WORKDIR /usr/src/app
    COPY package*.json ./
    RUN npm install --production
    COPY . .
    EXPOSE 3000
    CMD ["node", "server.js"]

---

## 🧱 Example: Python Flask Application
    FROM python:3.10-slim

    ENV PYTHONDONTWRITEBYTECODE=1
    ENV PYTHONUNBUFFERED=1

    WORKDIR /app
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    COPY . .

    EXPOSE 5000
    CMD ["python", "app.py"]

---

## 🧰 Example: Multi-Stage Build (Go Binary)
    FROM golang:1.22 AS builder
    WORKDIR /src
    COPY . .
    RUN go build -o app .

    FROM alpine:3.19
    WORKDIR /app
    COPY --from=builder /src/app .
    CMD ["./app"]

---

## 🧱 Example: Security Hardening
    FROM ubuntu:22.04

    # Create non-root user
    RUN groupadd -r app && useradd -r -g app app
    WORKDIR /app
    COPY . .
    RUN chown -R app:app /app
    USER app

    CMD ["./start.sh"]

---

## 🧰 Docker Commands (Reference)
| Task | Command | Description |
|------|----------|-------------|
| Build image | `docker build -t myimage:latest .` | Build from Dockerfile |
| Run container | `docker run -it myimage` | Start interactive container |
| List images | `docker images` | View local images |
| List containers | `docker ps -a` | Show running/stopped containers |
| Remove image | `docker rmi myimage` | Delete image |
| Remove container | `docker rm mycontainer` | Delete container |
| Access shell | `docker exec -it mycontainer /bin/bash` | Open terminal in container |
| Tag image | `docker tag myimage repo/myimage:v1` | Version image |
| Push image | `docker push repo/myimage:v1` | Upload to registry |

---

## 🧰 Best Practices
- Use lightweight base images (e.g., `alpine`, `slim`)  
- Combine `RUN` commands to reduce layers  
- Always pin base image versions for consistency  
- Use `.dockerignore` to exclude unnecessary files  
- Run as a non-root user for better security  
- Use `COPY` instead of `ADD` unless extracting archives  
- Use multi-stage builds to minimize final image size  
- Include health checks where possible  

---

## 🧠 Healthcheck Example
    HEALTHCHECK --interval=30s --timeout=5s --start-period=10s \
      CMD curl -f http://localhost:8080/health || exit 1

---

## 🔍 Resources
- **Docker Docs:** https://docs.docker.com/engine/reference/builder/  
- **Best Practices:** https://docs.docker.com/develop/develop-images/dockerfile_best-practices/  
- **Docker Hub:** https://hub.docker.com/  
- **Cheat Sheet:** https://github.com/wsargent/docker-cheat-sheet  

---

**Notes / Observations:**  
(Add your personal Docker tricks, build optimizations, or lessons learned here.)
