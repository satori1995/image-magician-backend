bind = "0.0.0.0:80"
max_requests = 10000
keepalive = 5
backlog = 2048
proc_name = "image-magician-backend"
workers = 2
worker_class = "uvicorn.workers.UvicornWorker"
loglevel = "info"
timeout = 120


