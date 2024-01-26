#!/bin/bash
# entrypoint.sh

nginx -V 2>&1 | awk -F 'configure arguments: ' '{printf $2}'
#/opt/test < awk -F 'configure arguments: ' '{print $2}' > /opt/test