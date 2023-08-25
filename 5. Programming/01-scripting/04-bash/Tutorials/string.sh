#!/bin/bash

BUFFETT="Life is like a snowball. The important thing is finding wet snow and a really long hill."
# write your code here
CHANGE1=${BUFFETT[@]/snow/foot}
# echo $CHANGE1
CHANGE2=${CHANGE1[@]// snow/}
# echo $CHANGE2
CHANGE3=${CHANGE2[@]/finding/getting}
# echo $CHANGE3

# SUBSTRING="w"
# expr index "$CHANGE3" "$SUBSTRING" # index is 57 for letter "w". Since we need the whole word "wet" (3 letters in total): 57+2=59

POS=0
LEN=59

ISAY=${CHANGE3:$POS:$LEN}


# Test code - do not modify
echo "Warren Buffett said:"
echo $BUFFETT
echo "and I say:"
echo $ISAY