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

- Command(s): `$PSversionTable`

## Century2

The password for Century3 is the name of the built-in cmdlet that performs the wget like function within PowerShell PLUS the name of the file on the desktop.

- Command(s): `Get-Alias wget`, `Get-Alias -Definition Invoke-WebRequest`, `dir`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/7fd3295d-2f31-4c8c-bb55-3f7e4ed4c681)
![image](https://github.com/gustavoalito/BeCode/assets/133368766/490eff57-0a90-460f-bf02-fcbc887ae80f)

## Century3

The password for Century4 is the number of files on the desktop.

- Command(s): Get-ChildItem | Measure-Object

## Century4

The password for Century5 is the name of the file within a directory on the desktop that has spaces in its name.

- Command(s): `Get-ChildItem -Recurse | Select-String ' '` => Found 2 files. Tried the 1st file's name and it worked.

## Century5

The password for Century6 is the short name of the domain in which this system resides in PLUS the name of the file on the desktop.

- Command(s): `Get-AdDomain | Select-Object Name` or simply `Get-AdDomain` and find the property requested. In this case, it's "Name".

## Century6

The password for Century7 is the number of folders on the desktop.

- Command(s): Get-ChildItem | Measure-Object


## Century7

The password for Century8 is in a readme file somewhere within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user’s profile.

- Command(s): `Get-ChildItem -Path C:\users\century7\contacts, C:\users\century7\desktop, C:\users\century7\documents, C:\users\century7\downloads, C:\users\century7\favorites, C:\users\century7\music, C:\users\century7\videos -Include *readme* -Recurse -ErrorAction SilentlyContinue`
- Found a file named *Readme.txt* in *C:\users\century7\downloads*. Showing its contents to reveal the password.
- Ref.: https://devblogs.microsoft.com/scripting/use-windows-powershell-to-search-for-files/

## Century8

The password for Century9 is the number of unique entries within the file on the desktop.
- Command(s): `(Get-Content .\unique.txt | Sort-Object -Unique).Length`
- Ref.: https://www.tutorialspoint.com/how-to-count-the-total-number-of-lines-in-the-file-in-powershell

## Century9

The password for Century10 is the 161st word within the file on the desktop.
- Command(s): `$century10 = (-split (Get-Content -Raw -Path C:\Users\Century9\Desktop\Word_File.txtWord_File.txt))[160]`, then call the variable `$century10`
- Ref.: https://stackoverflow.com/questions/58423984/century10-underthewire-tech-walkthrough
- This approach splits the file into words irrespective of line breaks. Note that the above loads the entire file into memory as a single string, using *-Raw*.

## Century10
The password for Century11 is the 10th and 8th word of the Windows Update service description combined PLUS the name of the file on the desktop.

- Command(s):
  - `Get-Service -DisplayName *update*` and locate the Windows Update service. Note its "Name" (wuauserv).
  
  - `Get-Service -DisplayName "Windows Update" | Select-Object *` Will list properties of the service, however, "Description" is not part of the list.
  
  - For that, we need to run the command `Get-CimInstace` to display information about the available class.
  
  - `Get-CimInstance -Class Won32_Service -Filter "Name='wuauserv'" | Select-Object *`. This will display all the properties of the Windows Update class. From there, you can manually count the words from the description.
  
  - Alternatively, if you want to display **only** the Description, then you need to amend the command and format it so it wraps the field: `Get-CimInstance -Class Win32_Service -Filter "Name='wuauserv'" | Select-Object -Property Description | ft -Wrap`.

## Century11
The password for Century12 is the name of the hidden file within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user’s profile.

NOTE:
– Exclude “desktop.ini”.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/8ff4dd86-751f-4f37-8461-8e6925885e04)

Following the contents of *users\century11*, I only searched for the directories present on the requested list. 

- Command(s): `Get-ChildItem -Path "C:\users\century11\Desktop", "C:\users\century11\Downloads", "C:\users\century11\Favorites", "C:\users\centu
ry11\Music", "C:\users\century11\Videos" -Hidden`

## Century12
The password for Century13 is the description of the computer designated as a Domain Controller within this domain PLUS the name of the file on the desktop.

- Command(s): `Get-AdComputer UTW -Properties *` and manually locate the property *Description*. *OR*, `Get-AdComputer UTW -Properties * | Select-Object Description`.
- First, we need to identify the computer's name. I identified 2 ways of doing it:
  1. `Get-AdDomainController` and locate the property *Name*;
  2. `Get-AdDomainController -Filter * | Select-Object Name`. This will give you the name, directly.
  Once located, we can use the name to run the necessary commands to find the computer's description.
-Ref.: https://activedirectorypro.com/list-all-domain-controllers-with-powershell/, https://shellgeek.com/get-ad-computer-description-using-powershell/

## Century13
The password for Century14 is the number of words within the file on the desktop.

- Command(s): `Get-Content .\countmywords | Measure-Object -Word`
- Ref.: https://devblogs.microsoft.com/scripting/use-a-powershell-cmdlet-to-count-files-words-and-lines/


## Century14
The password for Century15 is the number of times the word “polo” appears within the file on the desktop.

NOTE:
– You should count the instances of the whole word only.

- Command(s): `(Get-Content .\countpolos -Raw | Select-String -Pattern "\bpolo\b" -AllMatches).Matches.count`
- The regular expression `\bpolo\b` is used to match the whole word "polo" in a text. Let's break down the components of this regular expression:

The starting `\b` is a word boundary anchor. It represents the position between a word character and a non-word character. In this case, it ensures that "polo" is not part of a larger word and is surrounded by non-word characters or the beginning/end of the string. The ending `\b` is another word boundary anchor. It serves the same purpose as the first \b, ensuring that "polo" is not part of a larger word and is surrounded by non-word characters or the beginning/end of the string.

By using \b at the beginning and end of the word "polo", we ensure that only the whole word "polo" is matched, and not any partial matches within larger words.
