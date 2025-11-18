🐍 Python API: Cloud-Native ECS Deployment

1. Project Overview

This is a minimalist Python API. The primary feature of this project is its robust and automated CI/CD workflow, ensuring continuous, zero-downtime deployment to AWS Elastic Container Service (ECS) using the Fargate serverless compute engine. All traffic is managed and distributed via an Application Load Balancer (ALB).

2. Architecture

The API operates within a fully containerized, highly available environment. The pipeline automates the entire process from code commit to service update.

Key AWS Components:

AWS ECS Fargate: Runs the Python application in Docker containers without managing servers.

Application Load Balancer (ALB): Distributes incoming traffic across multiple running Fargate tasks.

AWS ECR: Stores the production-ready Docker images.