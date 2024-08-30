# me.backend

docker build -t me-backend .
docker tag me-backend:latest <account_id>.dkr.ecr.eu-west-1.amazonaws.com/me-backend-repo:latest
docker push <account_id>.dkr.ecr.eu-west-1.amazonaws.com/me-backend-repo:latest
aws ecs update-service --cluster me-backend-cluster --service me-backend-service --force-new-deployment --region eu-west-1


In order to run the backend/test you need two database

sudo -u postgres psql

CREATE USER your_db_user WITH PASSWORD 'password';

CREATE DATABASE backend;
CREATE DATABASE backend_test;

GRANT ALL PRIVILEGES ON DATABASE backend TO your_db_user;
GRANT ALL PRIVILEGES ON DATABASE backend_test TO your_db_user;