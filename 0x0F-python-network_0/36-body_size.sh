#!/bin/bash
curl -iLs '$1' | grep Content-Length | awk -F  "Content-Length: " '{print $2}'
