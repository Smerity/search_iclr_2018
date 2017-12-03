#!/bin/bash

# For local dev:
# export FLASK_DEBUG=1
# export FLASK_APP=server.py
# flask run

# To restart server, kill -HUP <pid>

mkdir log 2> /dev/null
DEBUG=0 authbind gunicorn -b 0.0.0.0:80 server:app --access-logfile log/access.log --error-logfile log/general.log
