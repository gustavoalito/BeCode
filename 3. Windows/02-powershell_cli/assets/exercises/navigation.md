# Powershell Navigation

Now we will learn how to move around in the filesystem with `Set-Location`, `Get-Location`, `Get-ChildItem` ...

![image](https://github.com/gustavoalito/BeCode/assets/133368766/00001014-4f5d-47f8-aec1-6a903273f35e)

- Print your current location on the screen

`pwd` => c:\Windows\system32
`Get-Location` works the same.
- Print the content of your current directory

  `ls` or `Get-ChildItem`
- Print the content of your root (`C:` _if you're running windows_, `/` _for linux_)

  `Get-ChildItem c:`
- Go into your home folder (_C:\Users\Username or /home/Username_)

  `Set-Location C:\Users\Username`
- Print the content of your home

  `Get-ChildItem`
- Those commands are pretty long to type, do you know any shorter way to do it?

  `PS C:\Windows\system32> Get-ChildItem -Path C:\Users\Username`
