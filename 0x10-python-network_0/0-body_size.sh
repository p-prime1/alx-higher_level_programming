#!/bin/bash
#Sends a request to a url and returns the size of the body
response=$(curl -s -w '%{size_download}\n' -o /dev/null "$1") echo "$response"
