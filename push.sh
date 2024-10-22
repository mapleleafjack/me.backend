#!/bin/bash

# Check if account_id is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <account_id>"
  exit 1
fi

# Set account_id to the first argument
account_id=$1

# Build the Docker image
docker build -t me-backend .

# Tag the Docker image
docker tag me-backend:latest ${account_id}.dkr.ecr.eu-west-1.amazonaws.com/me-backend-repo:latest

# Login to AWS ECR
aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin ${account_id}.dkr.ecr.eu-west-1.amazonaws.com

# Push the Docker image to ECR
docker push ${account_id}.dkr.ecr.eu-west-1.amazonaws.com/me-backend-repo:latest

# Force ECS to update the service
aws ecs update-service --cluster me-backend-cluster --service me-backend-service --force-new-deployment --region eu-west-1

# Invalidate CloudFront cache
aws cloudfront create-invalidation --distribution-id E1F6T02STMJGS9 --paths "/*"
