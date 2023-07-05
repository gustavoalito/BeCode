# Bandit Wargame
This is essentially a CTF (catch the flag) platform where the falg is the password for the next level. 

The Bandit wargame is aimed at absolute beginners. It will teach the basics needed to be able to play other wargames.
Reference: https://overthewire.org/wargames/bandit/

---
To get started, visit the reference link above and start with the level 0 to get acquainted with the system. Each level provides tips and material to help you solve it. 
You first need to connect via ssh. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. 

To get your started:

    ssh bandit0@bandit.labs.overthewire.org -p 2220

Every level will increase the bandit's username level in the ssh command. Since your username started with 0 (zero) - bandit0@... - once you obtain the password for the next level, you simply increase a number in your username:

    ssh bandit1@bandit.labs.overthewire.org -p 2220

---

The table below provides the level number, the command(s) used to find the password and the password itself. This is a work in progress where necessary walkthrough can be added depending on the level's complexity.

|Level|Command(s) used|Password|Comments
|--|--|--|--|
|0  |cat readme  |NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL  | - |
|1  |cat < -  |rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi  | - |
|2  |cat spaces\ in\ this\ filename or simply type in "cat spa" and use the tab to autocomplete  |aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG  |-  |
|3  |cat < .hidden  |2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe  |-  |
|4  |`cat -- /home/bandit4/inhere/-*` Password located in "-file07".  |lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR  |-  |
|5  |`find . -size 1033c` `cat < inhere/maybehere07/.file2`  |P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU  |-  |
|6  |`find / -user bandit7 -group bandit6 -size 33c` Locate the only file that doesn't display permission denied.  |z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S  |-  |
|7  |grep "millionth*" data.txt  |TESKZC0XvTetK0S9xNwm25STk5iWrBvP  |-  |
|8  |`sort data.txt | uniq -c` or `sort data.txt | uniq -c | grep -v "10"`  |EN632PlfYiZbn3PhVK3XOGSlNInNE00t  |-  |
|9  |`strings -a data.txt | egrep "=+"`  |G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s  |-  |
|10  |base64 -d data.txt  |6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM  |-  |
|11  |`cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`  |JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv  |-  |
|12  |?  |?  |To be continued. Quite complex: https://mayadevbe.me/posts/overthewire/bandit/level13/  |

// To be continued..


