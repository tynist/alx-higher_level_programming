#!/bin/bash
# Takes in a URL, sends request to it,
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
