#!/bin/bash
# Takes in a URL, sends request to it,
# and displays the size of the body of the response

curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
