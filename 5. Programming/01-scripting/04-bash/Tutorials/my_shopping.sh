#!/bin/bash
# Run this script with 6 space separated arguments. Ex.: bash my_shopping.sh apple 5 banana 8 "Fruit Basket" 15

echo "File name is "$0 # Holds the current script
echo $3 # $3 Holds banana
Data=$5
echo "A $Data costs just $6."
echo $# 
# $# prints the number of arguments passed
echo "The arguments passed to run the script were: $@"
