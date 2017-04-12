#!/bin/bash
# Sends a POST request to the URL, and displays the body of the response
curl -sLd "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
