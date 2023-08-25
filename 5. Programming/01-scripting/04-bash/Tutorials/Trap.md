# Trap

It often comes the situations that you want to catch a special signal/interruption/user input in your script to prevent the unpredictables.

Trap is your command to try:

`trap <arg/function> <signal>`

Example in file **trap.sh**

Some of the common signal types you can trap:

**SIGINT**: user sends an interrupt signal (Ctrl + C)

**SIGQUIT**: user sends a quit signal (Ctrl + D)

**SIGFPE**: attempted an illegal mathematical operation

You can check out all signal types by entering the following command:

`kill -l`

Notice the numbers before each signal name, you can use that number to avoid typing long strings in trap:

#2 corresponds to SIGINT and 15 corresponds to SIGTERM
`trap booh 2 15`
one of the common usage of trap is to do cleanup temporary files:

`trap "rm -f folder; exit" 2`