---
title: "<% tp.file.title %>"
type: tool-note
tool: Docker
created: "<% tp.date.now('YYYY-MM-DD') %>"
tags: [docker]
cssclass: cs-note
---

# <% tp.file.title %>

## Concept
Describe the image or Dockerfile change.

## Dockerfile Snippet
```dockerfile
FROM alpine:latest
RUN apk add --no-cache python3
CMD ["python3", "--version"]
```

## Commands
| Task | Command |
|------|---------|
| Build | `docker build -t myimage .` |
| Run | `docker run myimage` |
| List images | `docker images` |

## Notes
- 

## References
Docker Hub, docs

