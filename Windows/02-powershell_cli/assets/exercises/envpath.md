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
  _____________________________________________________________
| $csvPath = "C:\path\to\output.csv"                           |
|                                                              |
| $computerInfo = Get-ComputerInfo                             |
| $computerInfo | Export-Csv -Path $csvPath -NoTypeInformation |
_______________________________________________________________

The $csvPath variable stores the path where the CSV file will be saved. Make sure to modify it to the desired file path.

The Get-ComputerInfo cmdlet retrieves comprehensive computer information, including operating system details, hardware specifications, network configuration, and more.

The output of Get-ComputerInfo is assigned to the $computerInfo variable.

The $computerInfo variable is then exported to a CSV file using the Export-Csv cmdlet. The -NoTypeInformation parameter ensures that the CSV file does not include the type information.

I created a file on the Desktop named "computer-specs.ps1" and edited it via PowerShell ISE (right-click the file and select "Edit").

To run the script (considering I'm in the script's directory): `.\computer-specs.ps1`

Open the created CSV file.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/75ba9e76-5691-4a7a-ab9f-080660439207)

**Security considerations**
By default, PowerShell restricts the execution of scripts as a security measure. If you try to run the script after saving it, you might encounter an error related to the "execution policy."

To change the execution policy in a secure way, follow these steps:

Open an elevated PowerShell prompt by right-clicking on the PowerShell icon and selecting "Run as administrator."

Run the following command to check the current execution policy:
`Get-ExecutionPolicy`

If the current policy is set to "Restricted" or "AllSigned," you'll need to change it. Choose the policy that suits your needs but is still secure. For example, you can set the execution policy to "RemoteSigned" with the following command:
`Set-ExecutionPolicy RemoteSigned`

You'll be prompted to confirm the change. Type "Y" and press Enter.

Now you can run your script without encountering the execution policy restriction.

Remember to revert the execution policy back to a more secure setting after you've completed your task. You can set it back to "Restricted" with the following command: `Set-ExecutionPolicy Restricted`. This ensures that only trusted scripts can be executed on your system.

- Some reference: https://www.pdq.com/blog/writing-your-first-powershell-script/

> **WARNING**: This exercise will **only work on Windows** since it's specific to the way Windows manages environment variables.
