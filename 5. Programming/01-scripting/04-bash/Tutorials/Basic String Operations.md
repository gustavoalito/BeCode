# Basic String Operations

The shell allows some common string operations which can be very useful for script writing.

## String Length

`#       1234567890123456`
`STRING="this is a string"`
`echo ${#STRING}            # 16`

## Index

Find the numerical position in $STRING of any single character in $SUBSTRING that matches. Note that the 'expr' command is used in this case.

`STRING="this is a string"`
`SUBSTRING="hat"`
`expr index "$STRING" "$SUBSTRING"     # 1 is the position of the first 't' in $STRING`

## Substring Extraction

Extract substring of length $LEN from $STRING starting after position $POS. Note that first position is 0.

`STRING="this is a string"`
`POS=1`
`LEN=3`
`echo ${STRING:$POS:$LEN}   # his`

If :$LEN is omitted, extract substring from $POS to end of line

`STRING="this is a string"`
`echo ${STRING:1}           # $STRING contents without leading character`
`echo ${STRING:12}          # ring`

### Simple data extraction example:

`# Code to extract the First name from the data record`
`DATARECORD="last=Clifford,first=Johnny Boy,state=CA"`
`COMMA1='expr index "$DATARECORD" ',''  # 14 position of first comma`
`CHOP1FIELD=${DATARECORD:$COMMA1}       #`
`COMMA2='expr index "$CHOP1FIELD" ','' `
`LENGTH='expr $COMMA2 - 6 - 1' `
`FIRSTNAME=${CHOP1FIELD:6:$LENGTH}      # Johnny Boy`
`echo $FIRSTNAME`

### Substring Replacement

STRING="to be or not to be"
Replace first occurrence of substring with replacement

`STRING="to be or not to be"`
`echo ${STRING[@]/be/eat}        # to eat or not to be`

#### Replace all occurrences of substring

`STRING="to be or not to be"`
`echo ${STRING[@]//be/eat}        # to eat or not to eat`

#### Delete all occurrences of substring (replace with empty string)

`STRING="to be or not to be"`
`echo ${STRING[@]// not/}        # to be or to be`

#### Replace occurrence of substring if at the beginning of $STRING

`STRING="to be or not to be"`
`echo ${STRING[@]/#to be/eat now}    # eat now or not to be`

#### Replace occurrence of substring if at the end of $STRING

`STRING="to be or not to be"`
`echo ${STRING[@]/%be/eat}        # to be or not to eat`

#### Replace occurrence of substring with shell command output

`STRING="to be or not to be"`
`echo ${STRING[@]/%be/be on $(date +%Y-%m-%d)}    # to be or not to be on 2012-06-14`