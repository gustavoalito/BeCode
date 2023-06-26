# Exercise Powershell CLI - Trial of might

Now that you gathered some basic understanding of the Powershell CLI, here is an exercise to test your might! It's been put together by the guys at [UnderTheWire](https://underthewire.tech/) (_very similar to OverTheWire_). You will have to tackle a series of exercises called Century that is aimed at testing the fundamentals of Powershell know-how.

- Go to the webpage of the [Century game](https://underthewire.tech/century) and follow the instructions there
- **complete a maximum amount of levels** and **take note of the passwords** for each one of them
- First level:  ```century1@century.underthewire.tech``` 
- Password: ```century1```
- Encrypt the collected passwords with GPG, upload them on GitHub with a minimalist readme, and send me your public key. 

---

## Century1

The password for Century2 is the build version of the instance of PowerShell installed on this system.

- Password:
- Command(s): `$PSversionTable`

## Century2

The password for Century3 is the name of the built-in cmdlet that performs the wget like function within PowerShell PLUS the name of the file on the desktop.

- Password:
- Command(s): `Get-Alias wget`, `Get-Alias -Definition Invoke-WebRequest`, `dir`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/7fd3295d-2f31-4c8c-bb55-3f7e4ed4c681)
![image](https://github.com/gustavoalito/BeCode/assets/133368766/490eff57-0a90-460f-bf02-fcbc887ae80f)

## Century3

The password for Century4 is the number of files on the desktop.

- Password:
- Command(s): Get-ChildItem | Measure-Object

## Century4

The password for Century5 is the name of the file within a directory on the desktop that has spaces in its name.

- Password:
- Command(s): `Get-ChildItem -Recurse | Select-String ' '` => Found 2 files. Tried the 1st file's name and it worked.

## Century5

The password for Century6 is the short name of the domain in which this system resides in PLUS the name of the file on the desktop.

- Password:
- Command(s): `Get-AdDomain | Select-Object Name` or simply `Get-AdDomain` and find the property requested. In this case, it's "Name".

## Century6

The password for Century7 is the number of folders on the desktop.

- Password:
- Command(s): Get-ChildItem | Measure-Object


## Century7

The password for Century8 is in a readme file somewhere within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user’s profile.

- Password: 
- Command(s): `Get-ChildItem -Path C:\users\century7\contacts, C:\users\century7\desktop, C:\users\century7\documents, C:\users\century7\downloads, C:\users\century7\favorites, C:\users\century7\music, C:\users\century7\video
s -Include *readme* -Recurse -ErrorAction SilentlyContinue`
- Found a file named *Readme.txt* in *C:\users\century7\downloads*. Showing its contents to reveal the password.
- Ref.: https://devblogs.microsoft.com/scripting/use-windows-powershell-to-search-for-files/

## Century8

The password for Century9 is the number of unique entries within the file on the desktop.
- Password: 
- Command(s): `(Get-Content .\unique.txt | Sort-Object -Unique).Length`
- Ref.: https://www.tutorialspoint.com/how-to-count-the-total-number-of-lines-in-the-file-in-powershell

## Century9

The password for Century10 is the 161st word within the file on the desktop.
- Password: 
- Command(s): `$century10 = (-split (Get-Content -Raw -Path C:\Users\Century9\Desktop\Word_File.txtWord_File.txt))[160]`, then call the variable `$century10`
- Ref.: https://stackoverflow.com/questions/58423984/century10-underthewire-tech-walkthrough
- This approach splits the file into words irrespective of line breaks. Note that the above loads the entire file into memory as a single string, using *-Raw*.

## Century10

- Password: 
- Command(s):


