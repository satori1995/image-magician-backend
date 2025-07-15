FROM python:3.12

WORKDIR /app
COPY lib/ /app/lib/
COPY scripts/run_server.sh /app/run_server.sh
COPY scripts/gunicorn.py /app/gunicorn.py
COPY requirements.txt /app/
RUN python -m venv .venv && .venv/bin/pip install -r requirements.txt
CMD ["bash", "/app/run_server.sh"]
