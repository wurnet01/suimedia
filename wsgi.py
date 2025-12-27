"""
WSGI entry point for hosting platforms (PythonAnywhere, Heroku, etc.).

Configure the web host to use the WSGI callable named `application` from this file.

On PythonAnywhere set environment variables `SECRET_KEY` and optionally `DATABASE_URL`.
"""
from app import app

# WSGI servers expect the callable to be named `application`.
application = app
