#!/bin/bash
# Displays all HTTP methods the server will accept
curl -isL -X OPTIONS "$1" | grep "Allow" | awk -F ": " '{print $2}'
