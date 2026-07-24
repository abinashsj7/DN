# Docker Architecture

Docker consists of three main components.

## 1. Docker Client

Used to execute Docker commands.

Example:

docker run

docker build

docker pull

---

## 2. Docker Daemon

Processes Docker commands.

Responsible for:
- Building images
- Running containers
- Managing Docker resources

---

## 3. Docker Registry

Stores Docker Images.

Example:

Docker Hub

---

## Architecture Diagram

Docker Client
       │
       ▼
Docker Daemon
       │
       ▼
Docker Registry
       │
       ▼
Docker Images
       │
       ▼
Docker Containers
