#!/bin/bash
# Displays only the status code of the response
curl -Ils | grep HTTP | awk -F " " '{print $2}'
