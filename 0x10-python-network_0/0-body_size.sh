response=curl -sI $1 | grep -I Content-Length
echo response
