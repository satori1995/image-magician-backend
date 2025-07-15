#!/bin/bash
exec gunicorn -c gunicorn.py lib.app:app
