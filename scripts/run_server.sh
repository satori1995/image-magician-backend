#!/bin/bash
exec ./venv/bin/gunicorn -c gunicorn.py lib.app:app
