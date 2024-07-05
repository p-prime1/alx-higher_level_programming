#!/bin/bash
#Sends a request to a url and returns the size of the body
response=$(curl -sI "$1" | grep -i "Content-Length") echo "$response"
