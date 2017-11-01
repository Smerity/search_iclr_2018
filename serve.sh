#!/bin/bash
# To restart server, kill -HUP <pid>
mkdir log 2> /dev/null
DEBUG=0 authbind gunicorn -b 0.0.0.0:80 server:app --access-logfile log/access.log --error-logfile log/general.log
