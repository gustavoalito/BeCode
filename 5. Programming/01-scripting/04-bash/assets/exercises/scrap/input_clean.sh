#!/bin/bash

cat input.txt | tail -n+32 | head -n-24 > input_cleaned.txt
sed '/\[item\]/d; /\_/d; /[0-9]\+ reviews/d' input_cleaned.txt > output.txt
# The "sed" command deletes lines that contain [item], an underscore, as well as lines that match the pattern of having one or more digits followed by "reviews".