#!/bin/bash
#Sends a request to a url and returns the size of the body
curl -s -w  "$1" | wc -c
