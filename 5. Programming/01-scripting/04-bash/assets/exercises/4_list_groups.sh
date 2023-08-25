#!/bin/bash

user=$(whoami)
groups=$(groups)

echo "Your username is:" $user

for group in $groups; do
    echo $user is part of the group $group
    ((count++))  # Increment the count for each group
done

echo "Total number of groups: $count"  # Display the total count