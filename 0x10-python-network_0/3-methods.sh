#!/bin/bash
#Accepts a url and returns all the methods available for it
curl -sX OPTIONS "$1"
