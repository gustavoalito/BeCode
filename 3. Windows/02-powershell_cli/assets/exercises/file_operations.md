# Powershell File Operations

Now that we know how to move in the file system, let's check how to manipulate files and folders. In this challenge, you will discover and use the commands `Get-Content`, `echo`, `New-Item`, `Move-Item`, `Copy-Item`, and `Remove-Item`.

- Create a file named story1.txt

`New-Item story1.txt`
- Type `echo "Hello World" > story1.txt`
- Print the content of the file

`Get-Content story1?.txt` or `Get-Content ./story1.txt`
- Create a folder named `story`

You need to specify the type. `New-Item story -Type Directory`
- Move `story1.txt` inside `story`

`Move-Item story1.txt story`
- Copy `story1.txt` as `story2.txt`

`Copy-Item .\story\story1.txt .\story\story2.txt`
- Print both files

`Get-Content story1.txt,story2.txt`
- Rename `story2.txt` as `me.txt`

`Rename-Item story2.txt me.txt`
- Append `me.txt` and add "I am a junior at Becode"

`echo "I am a junior at BeCode" >> me.txt`
- Remove the folder story with its content

`Remove-Item story` And answer "Y" or "A".
Or `Remove-Item –path c:\users\username\story –recurse `
