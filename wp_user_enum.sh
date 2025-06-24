#!/bin/bash

# Simple script to extract the users registered in a Wordpress web.

if [ "$#" -ne 2 ]; then
    echo $#
    echo "USAGE: ./wp_user_enum.sh URL MAX_ID"
    exit 1
fi

URL="${1}?author=" #"http://localhost/wordpress/?author="

MAX_USR_ID=$2 # 10

echo "Extracting users from ${1}"

for i in $(seq 1 $MAX_USR_ID); do
    curl -I -s "${URL}${i}" | grep -i "Location:" | awk -F '/' '{ print $(NF-1) }'
done


