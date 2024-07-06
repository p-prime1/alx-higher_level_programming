#!/bin/bash
#Sends a DELETE request to a url passed as an argument
response_code=$(curl -s -X DELETE "$1") echo $response_code
