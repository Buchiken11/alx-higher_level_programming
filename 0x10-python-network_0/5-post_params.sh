#!/bin/bash
#Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
#
url="$1"
email="test@gmail.com"
subject="I will always be here for PLD"

# Send a POST request with the variables and display the response body
curl -sL -X POST -d "email=$email&subject=$subject" "$url"
