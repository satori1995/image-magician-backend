# /bin/bash
git pull
docker rm -f image-magician-backend
docker rmi -f image-magician-backend
docker build -f Dockerfile -t image-magician-backend . --no-cache
docker run --name image-magician-backend -p 10001:80 -d image-magician-backend


