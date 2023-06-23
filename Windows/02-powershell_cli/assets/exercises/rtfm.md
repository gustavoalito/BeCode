# Powershell RTFM

Everybody needs a little help at one time or another. In this exercise, we will check how you can get help on Powershell and how you can find interesting commands following your needs.

- Open a PowerShell session in your terminal
- type `Get-Help`
- Find out what a command such as `Get-Process` does without looking on Google
  `Get-Process -?` => The "Get-Process" cmdlet gets the processes on a local or remote computer. 
- Now try with the `-online` parameter
  `get-help Ger-Process -online` will open the browser to display the command's online library.
- What does `Get-command` do?
  `Get-Command -?` => The Get-Command displays all the cmdlets, functions, and aliases installed on the computer.

Optionally:

- Try to get help on common commands such as `ls`, `cp`, `mv`, ...

Just use the command name + -? to display its help. Example `ls -?`
