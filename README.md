# Myapp

**Pre-Req:**

1. Python 3.7 (only if running locally)
2. Docker with K8s

**Run Locally:**

1. Unzip
1. cd to /myapp
1. Create Image using `docker build . -t myapp`
1. Create Service using `kubectl apply -f deployment.yml`
1. Navigate to <http://localhost:6000>