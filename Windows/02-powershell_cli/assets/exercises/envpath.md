# Powershell Environment Variables

In any programming language, you can store data within variables. However they only exist as long as the program is executed, but what if you wanted to share information between two applications not running at the same time?

Then you could use environment variables, which are variables stored at the OS level. You can access them from anywhere.

- Open a Powershell Terminal
- Type `echo $env:computername`. It should show your computer's name
- Create a variable by typing `$env:test = "hello powershell"`
- Check the variable you just created the same way you did with the computer name
- Now we will add something to this variable by typing `$env:test += " Becode"`
- Check the variable
- There is one really important environment variable: `$env:path`. This variable stores the location where Windows looks for files that are not in your current folder. For example, if you call VSCode from the PowerShell terminal, it opens it even if the executable isn't present in the current folder. That's because the path to the vscode's executable is stored in `$env:path`. Now download an executable software ([rufus](https://github.com/pbatard/rufus/releases/download/v3.13/rufus-3.13p.exe) for example) and copy it on your desktop. If you try from a command line to launch it, it will fail with a command not found (if you are not in the same folder).
- Try to append the $env:path by adding the path to rufus' executable (it should be something like this if you copied it on your desktop: `C:\Users\Username\Desktop`)

![image](https://github.com/gustavoalito/BeCode/assets/133368766/7ed3adee-4da8-4464-87ba-ddef0cb2be13)

- Try to call rufus from anywhere

![image](https://github.com/gustavoalito/BeCode/assets/133368766/883d745d-81b0-40e5-8835-d82f22b4c08d)

- I would like you to have a look at [the recognized environment variables available on Windows](https://docs.microsoft.com/en-us/windows/deployment/usmt/usmt-recognized-environment-variables).
- Write a small script reporting your computer specs and convert it into a CSV file. You might have some trouble executing your script once saved. Why? How can you change it in a secure way?

Script:

| $csvPath = "C:\path\to\output.csv" |

$computerInfo = Get-ComputerInfo
$computerInfo | Export-Csv -Path $csvPath -NoTypeInformation


> **WARNING**: This exercise will **only work on windows** since it's specific to the way windows manages environment variables.
