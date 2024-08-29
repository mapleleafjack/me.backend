# me.backend

docker build -t me-backend .
docker tag me-backend:latest <account_id>.dkr.ecr.eu-west-1.amazonaws.com/me-backend-repo:latest
docker push <account_id>.dkr.ecr.eu-west-1.amazonaws.com/me-backend-repo:latest
aws ecs update-service --cluster me-backend-cluster --service me-backend-service --force-new-deployment --region eu-west-1