#!/bin/bash

# Compare three lists of arrays and write the common elements of all three arrays. The result is the common element 5.

a=(3 5 8 10 6)
b=(6 5 4 12)
c=(14 7 5 7)

for number in "${a[@]}"; do
    found_in_b=false
    found_in_c=false

    for num_b in "${b[@]}"; do
        if [ "$number" -eq "$num_b" ]; then
            found_in_b=true
            break
        fi
    done

    for num_c in "${c[@]}"; do
        if [ "$number" -eq "$num_c" ]; then
            found_in_c=true
            break
        fi
    done

    if $found_in_b && $found_in_c; then
        echo "$number"
    fi
done  
