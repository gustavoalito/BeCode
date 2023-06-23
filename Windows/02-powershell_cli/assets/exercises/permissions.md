# Powershell Permissions

Now that we can navigate and create files, we should be able to change permissions on these. We will use the commands `Get-Acl`, `Set-Acl`, `RunAs`

- Create a file

`Net-Item Gustavo.txt`
- Check the owner and the groups

`Get-Acl Gustavo.txt`
- Change the file owner to the built-in administrator (administrator account is disabled by default, check how to enable it. Don't forget to set a strong password!)

The usual way:
`$acl = Get-Acl Gustavo.txt
$acl.setOwner([System.Security.Principal.NTAccount]::new("Administrator"))
Set-Acl Gustavo.txt $acl
Get-Acl Gustavo.txt`
- Check the file's permission

![image](https://github.com/gustavoalito/BeCode/assets/133368766/2b090793-9544-48d1-aba2-8af96264ebf6)

Alternative way:
![image](https://github.com/gustavoalito/BeCode/assets/133368766/3244a4ac-387e-44ee-8469-3ae8e6a9a1eb)

- Try to print the content of the file as your normal user

`Nothing happens.`
- Print the content of the file using the "administrator" account

To run as the Administrator user: `runas /user:Administrator" "powershell"`

This will prompt the user to type in the Administrator's password. Once typed in, a new PowerShell window will open and you're logged in as Administrator. 

`Set-Location c:\Users\Boss
Get-ChildItem
Get-Acl Gustavo.txt`


> **WARNING**: This exercise **will only work on Windows** system since file system permissions are not managed the same way on Windows and Linux.
