#!/bin/bash
#Returns the body if a status code of 200 is returned
response_code=$(curl -s -o /dev/null -w "%{http_code}" "$1"); [ "$response_code" -eq 200 ] && curl $1
