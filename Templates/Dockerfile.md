---
title: "Dockerfile"
type: docker
tags: [docker]
cssclass: cs-note
---

# Dockerfile Template

## Overview
Common directives and patterns for building images.

## Basic Structure
```dockerfile
FROM python:3.11-slim
LABEL maintainer="you@example.com"
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]
```

## Common Directives
| Directive | Description | Example |
|----------|-------------|---------|
| FROM | Base image | `FROM alpine:latest` |
| WORKDIR | Working directory | `WORKDIR /usr/src/app` |
| COPY | Copy files | `COPY . /app` |
| RUN | Build step | `RUN apt-get update` |
| ENV | Environment var | `ENV PORT=8080` |
| EXPOSE | Document port | `EXPOSE 8080` |
| CMD | Default command | `CMD ["node", "server.js"]` |
| ENTRYPOINT | Fixed main command | `ENTRYPOINT ["python3"]` |

## Multi-stage Example (Go)
```dockerfile
FROM golang:1.22 AS builder
WORKDIR /src
COPY . .
RUN go build -o app .

FROM alpine:3.19
WORKDIR /app
COPY --from=builder /src/app .
CMD ["./app"]
```

## Best Practices
- Use slim/alpine base images
- Combine RUN steps
- Add .dockerignore
- Run as non-root where possible

## References
Docker docs and best practices

