# FLAGS and extraction method

> # Edgar Allan Poe
BC{3d54r_4ll4n_P03_FL45}
- Go to /var/www/ and open index.html with a text editor.
- Another method is to use the student's machine's IP address in the browser. The page rendered will be blank. However, if you right-click anywhere and inspect the page, drilling down the "head" section, you'll find the poem and the flag underneath it.
> # GREP ME LOREM
BC{GREP_ME_LOREM_FL4G}
- Grep the lorem file.
	- grep "BC{*" lorem.txt
	- Search all sequences containing "Loxondota" in /home/student/lorem.txt
		- Command: grep "Loxondota" lorem.txt

> # Which command becode
BC{WH1CH_FL4G_EXECUTLE_FILE}
- Command: which becode

> # Export bash flag
BC{EXPORT_B4SH_FLAG}
- Command: env

> # Password file
BC{PASSWORD_FILE}
- located at: /var/www/html/a/b/c/d/e/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x/y/z/password.txt.
- Command: find / -type f -name password.txt
	- OR: find / -type f -name "password.txt" 2>/dev/null | grep "password.txt"
	- OR: locate password.txt

> # Find partial path
BC{FLAG_FIND_PARTIAL_PATH}
- Command: find / -type f -name "becode-*.sh" 2>/dev/null
- This command is also located in the ".history" file, line 27.

> # Samba flag
BC{}
- This flag is not avaulable in the system.

> # Root Flag 01-Linux
BC{}
- In progress...
