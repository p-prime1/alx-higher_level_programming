#!/bin/bash
#Accepts a url and returns all the methods available for it
echo $(curl -s -X OPTIONS "$1")
