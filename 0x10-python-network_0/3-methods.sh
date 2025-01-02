#!/bin/bash
#Accepts a url and returns all the methods available for it
curl -sX OPTIONS -I "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
