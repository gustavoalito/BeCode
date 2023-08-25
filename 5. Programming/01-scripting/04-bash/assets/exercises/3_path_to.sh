#!/bin/bash

# Check if an argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <path>"
    exit 1
fi

# Store the provided path
path=$1

# Check if the path exists
if [ ! -e "$path" ]; then
    echo "Error: Path '$path' does not exist."
    exit 1
fi

# Check if the path is a file
if [ -f "$path" ]; then
    echo "Content of file '$path':"
    cat "$path"
elif [ -d "$path" ]; then
    echo "Listing content of directory '$path':"
    ls "$path"
else
    echo "Error: '$path' is neither a file nor a directory."
fi