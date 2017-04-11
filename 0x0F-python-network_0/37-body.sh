#!/bin/bash
curl -Ils www.amazon.com | grep Content-Length | awk -F  "Content-Length: " '{print $2}'
