# Dockerfile

## What is a Dockerfile?

A Dockerfile is a text file containing instructions used to build a Docker Image.

---

## Sample Dockerfile

```dockerfile
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
```

---

## Common Instructions

FROM
- Base image

WORKDIR
- Sets working directory

COPY
- Copies files

RUN
- Executes commands during build

CMD
- Default command when the container starts

EXPOSE
- Opens a port

ENV
- Defines environment variables
