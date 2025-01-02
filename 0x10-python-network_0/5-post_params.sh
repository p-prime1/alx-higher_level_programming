#!/bin/bash
#Sending a post request using curl
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
