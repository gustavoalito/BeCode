#!/bin/bash
# Pass "Shell is fun" (3 arguments) to the script(prog.sh) as an argument and print the length of the arguments.

function File {
    # think you are inside the file
    # Change here
    echo "File name is:" $0
    echo "Number of arguemnts passed:" $#
}

# Do not change anything
if [ ! $# -lt 1 ]; then
    File $*
    exit 0
fi

# change here
# here you can pass the arguments
bash prog.sh Shell is fun
