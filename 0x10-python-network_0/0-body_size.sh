response=$(curl -sI "$1" | grep -i "Content-Length")
echo "$response"
