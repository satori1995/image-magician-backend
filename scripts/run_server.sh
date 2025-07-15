#!/bin/bash
./venv/bin/gunicorn -c gunicorn.py lib.app:app
