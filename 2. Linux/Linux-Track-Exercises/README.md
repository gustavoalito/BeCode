# Linux Track Exercises
Lixux Track Exercises answers
---
Connect to the virtual machine 10.12.181.X with the following credentials:
* **ip** : 10.12.181.X
* **user** : student
* **password** : student
# Finding Files with Linux
---
# Finding Files with Linux
## Exercises 
1. Create a file named ``my-file.txt`` with the touch command. Then execute the ``locate my-file.txt`` command. Do you find the file? 
    > Your response : NO.
1. Run the command sudo ``updatedb``. And run the locate my-file.txt command again. Do you find your file ?
    > Your response : YES.
1. With the command ``which``, find the executable file nc and indicate the path
    > Path : /bin/nc
1. With the command ``which``, find the executable file becode. What is the flag ?
    > Flag : BC{WH1CH_FL4G_EXECUTLE_FILE}
1. Search with ``find ``command for a file that contains the name "Edgar Allan Poe". What is the flag ?
    > Flag : BC{3d54r_4ll4n_P03_FL45}. I went to the page 10.12.181.91 and inspected the page.
1. Using the ``find`` command, find the file password.txt and specify the flag.
    > Flag : BC{PASSWORD_FILE} located at: /var/www/html/a/b/c/d/e/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x/y/z/password.txt. Command used: find / -type f -name password.txt
	OR: find / -type f -name "password.txt" 2>/dev/null | grep "password.txt"
1. With the command ``find``, find a file that starts with ``becode-`` and ends with ``.sh``.
    > Flag : BC(YOU_C4N_FIND_ME_WITH_WICH_IF_AM_EXEC). If you use the command which becode, you get the flag BC{WH1CH_FL4G_EXECUTLE_FILE}
1. Using the ``find`` command to identify any file (not directory) modified in the last day, NOT owned by the root
user and execute ls -l on them. **Chaining/piping commands is NOT allowed!**
    > Your command : find -type f -mtime 0 ! -user root => Explanation: 
	This command will find all regular files (-type f) that have been modified in the last day (-mtime 0) and are not owned by the root user (! -user root).
1. With the find command, find all the files that have an authorization of ``0777``.
    > Your command: find / -type f -perm 0777
1. With the find command, find all the files in the folder ``/home/student/findme/`` that have an authorization of ``0777`` and change the rights of these files to ``0755``
    > Your commands: find /home/student/findme -type f -perm 0777
2 ways to change their permissions. The general way would be to use the chmod command with the find command:
find /home/student/findme -type f -perm 0777 -exec chmod 0755 {} +
-exec chmod 0755 {} +: This part of the command executes the chmod command and changes the permissions of the found files to 0755. The {} placeholder is replaced by the filenames found by find.
2nd way. Since all the files within the findme directory have the same 0777 permission and have the same extension (.tx), we can simplify and use the following command: chmod 0755 /home/student/findme/*.tx
---
# Text manipulation with Linux
## Exercises 

1. Search all sequences containing "Loxondota" in ``/home/student/lorem.txt``
    > Flag : BC{GREP_ME_LOREM_FL4G}
	Command: grep "Loxondota" lorem.txt
1. Copy the file /etc/passwd to your home directory. Display the line starting with ``student`` name.
    > Your commands : cp /etc/passwd /home/student
	grep "^student" passwd
1. Display the lines in the passwd file starting with login names of 3 or 4 characters.
    > Your commands : egrep "^.{3,4}:" passwd
	> "^.{3,4}:" matches lines that start (^) with any character (.) repeated 3 to 4 times ({3,4}) and followed by a colon (:).
1. In the file ``/home/student/sample.txt`` how many different values are there in the first column? in the second?
    > Your response : 1st column: 4. 2nd column: 4
    > Your commands : cut -d "," -f 1 sample.txt | sort -u
	cut -d "," -f 2 sample.txt |sort -u
1. In the file ``/home/student/sample.txt`` sort the values in the second column by frequency of occurrence. (uniq -c can be useful)
    > Your response : 
	4 20
	2 10
    1 30
	1 11
    > Your command : cut -d "," -f 2 sample.txt | sort | uniq -c | sort -r
1. In the file ``/home/student/iris.data`` Change the column separator (comma) to tab (make sure that the changes are applied to the file)
    > Your response : sed is the command used for stream editing and text transformations. -i is an option that tells sed to edit the file in-place, making changes directly to the file rather than just displaying the modified output.
's/,/\t/g' is the sed substitution command. It replaces all occurrences of the comma , with a tab \t. /g tell it to make the changes globally in the file, not only in the 1st occurrence.
    > Your command : sed -i "s/,/\t/g" iris.data
1. In the file ``/home/student/iris.data``, extract from this file the column 3 (petal length in cm) (use cut )
    > Your response : See comment below. I extracted the column and saved it into a file named petal.txt
    > Your command : cut -f 3 iris.data > petal.txt
1. In the file ``/home/student/iris.data``, count the number of flower species (cut and uniq)
    > Your response :  
	1 (empty line)
    50 Iris-setosa
    100 Iris-versicolor
    50 Iris-virginica
    > Your command : cut -f 5 iris.data | sort | uniq -c
1. In the file ``/home/student/iris.data``, sort by increasing petal length (see sort options)
    > Your response : Use the -k option to sort on a certain column. For example, use " -k 2 " to sort on the second column.
    > Your command : sort -k 4 iris.data
1. In the file ``/home/student/iris.data``, show only lines with petal length greater than the average size
    > Your response : awk -F'\t' '{sum+=$4; count++} END {avg=sum/count}' <filename> > iris_avg: This calculates the average of values in the fourth column and redirects the output to a file named iris_avg.
awk -F'\t' 'NR==FNR {avg=$1; next} $4 > avg' iris_avg <filename>: This awk command reads the average value from the iris_avg file. In the first block NR==FNR {avg=$1; next}, it assigns the first field value from iris_avg to the variable avg. In the second block $4 > avg, it compares each value in the fourth column with the average value. If the value is greater than the average, it prints the line.
the NR==FNR {avg=$1; next} part of the command checks if awk is processing the first file (iris_avg). If true, it assigns the first field value of the current record (line) from the iris_avg file to the variable avg.
NR==FNR: This condition is true only when awk is processing the first file (iris_avg). In other words, it checks if the current input record number (NR) is equal to the input record number of the current file (FNR).
    > Your command : awk -F'\t' '{if($4>1.2305) print $4}' iris.data | sort
	awk -F'\t' 'NR==FNR {avg=$1} $4 > avg' iris_avg iris.data | sort -k 4
	> Some awk NR==FNR additional reference: https://www.baeldung.com/linux/awk-multiple-input-files#:~:text=NR%20and%20FNR%20are%20two,in%20the%20current%20input%20file.&text=The%20output%20above%20shows%20us,FNR%20are%20always%20the%20same
	
1. Using ``/etc/passwd``, extract the user and home directory fields for all users on your student
machine for which the shell is set to ``/bin/false``. 
    > Your response : We can first start by replacing the colon character to tabs. This way we'll have 7 columns in the file. Extract it to a new file named passwd_Column.
	Then use grep to find only the occurrences of "/bin/false" and output it into a file named passwd_bin.
	Since we have to extract columns 1, 6 and 7, we can use the cut command and output it into a file named passwd_cut.
	You can also sort by a column to make it look nice, but it's optional.
	OR: do it all with one command using pipe to transfer outputs from one command as an input to the next one. Let's try that:
	sed "s/:/\t/g" passwd | grep ""/bin/false" | cut -f 1,6,7 | sort -k 1 > passwd_final1
	And check for any differences.
    > Your command: sed "s/:/\t/g" passwd > passwd_Column
	grep "/bin/false" passwd_Column > passwd_bin
	cut -f 1,6,7 passwd_bin > passwd_final
	OR: sed "s/:/\t/g" passwd | grep ""/bin/false" | cut -f 1,6,7 | sort -k 1 > passwd_final1
	diff passwd_final passwd_final1
---
# Linux : Piping and Redirection
## Exercises

Read the following [article](https://ryanstutorials.net/linuxtutorial/piping.php) and answer the questions below. Some questions will require additional research.

1. Write the message "hello everyone" in a file called "test" by redirecting the output of the echo command.
    > Your command : echo "hello everyone" > test
1. Write the message "goodbye" in the same file "test" by redirecting the output of the echo command and without overwriting the content of "test" and check with the cat command
    > Your command : echo "goodbye" >> test
1. Make the ``ls -la`` command redirect to the ``foo`` file
    > Your command : ls -la > foo
1. Execute ``find /etc -name *conf*`` command  and redirect errors (only errors) to a file named err.txt 
    > Your command : find /etc -name *conf* 2>err.txt
1. Repeat the previous exercise, this time redirecting the errors to the linux nothingness.
    > Your command : find /etc -name *conf* 2>/dev/null
1. Now redirect the standard output and the error output of the ``find /etc -name *conf*`` command to two different files (std.out and std.err)
    > Your command : find /etc -name *conf* 2>std.err 1>std.out
	Ref.: https://linuxhint.com/redirect-stdout-and-stderr-to-file/
1. What does the mkfifo command do?
    > No answer required. It creates named pipes (FIFOs) with the given NAMEs.
1. Create a pipe named "MyNamedPipe". Then execute the pwd command which will transmit the data in this pipe. Then use the cat command to read the contents of your "MyNamedPipe" pipe.
    > Your commands : mkfifo MyNamedPipe
	pwd | MyNamedPipe
	cat MyNamedPipe
	> Comments: The best way of doing this is by tailing the created pipe. Open a new tab and type the following:
	tail -f MyNamedPipe
	Go back to the 1st tab and execute the commands described in this exercise. You'll note that once you send the pwd command output to the pipe, yit will be displayed in the 2nd tab. 
	What's interesting is that if you check the file's size after sending data to it, the file size is still zero. Why is that? Becuase a pipe receives data and serves data bidirectionally at once, and then the data is no longer stored in the pipe. This is the main concept of a pipe.
	Ref.: https://dev.to/0xbf/use-mkfifo-to-create-named-pipe-linux-tips-5bbk
1. With cat command, add number to the lines in the file /etc/passwd with the command ``nl``
    > Your commands : nl --help (to understand the commands that are possible and how it works).
	cat -n < passwd
	nl passwd > passwd_lined (assuming this file has already been created) 
1. Using the previous nl command, the head and tail commands, display the lines of /etc/passwd between line 7 and line 12
    > Your commands : ''nl /etc/passwd | tail -n +7 | head -n 6''
	
Comments: nl will enumerate the lines of the given file. 

- "tail -n +7" will dispplay lines starting from line 7. 
- "head -n 6" will display the first 6 lines (7 to 12).

      7  man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
      8  lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
      9  mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
      10 news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
      11 uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
      12 proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
--- 
  # Bash environnement
  ### Exercises 

1. On your student machine what is the value of the FLAG environment variable ?
> FLAG : BC{EXPORT_B4SH_FLAG}

1. Currently if you notice your machine, the variable you have created will be deleted. What should you do to make your variable persistent? (With a Bash shell).
> Commands : export VARTEST="This is a test variable."
			bash
			echo $VARTEST
			exit
			env
> Note that the exported variable is listed as part of the environment variables. If you logout, then the variable no longer exists.
  
  ### Exercises :

1. **From a hacker's perspective**, look for information that might be useful to you in the ``.history`` file. 
> Your answer: You can find usernames and passwords. For instance in line 118 there is a command: telnet 10.21.55.98 -login admin -pass MyP4ssW0rDiS3CuR3! You can also find patterns of the victim, files and applications. It is good to build a profile.
1. **From an analyst's perspective**, look for information that might be useful to you in the ``.history`` file. 
> Your answer: There is a backdoor script running in the machine, it requires further information. It provides tips to files edited that might contain important information as well as IP addresses that might have an open connection to this machine. One telnet connection with credentials and password in clear text (red flag here).
---
 # Protocols and servers
 ## Exercises
  1.  On your kali (or other) , install ``ngnix`` to have an http server on port 8080. Replace the default page of ngnix by an html page displaying a hello world.
    > Once you install Nginx and start it, it will still display apache2's default page when you open your browser and type localhost. 
	What needs to be done is described in here: https://askubuntu.com/questions/642238/why-do-i-still-see-an-apache-site-on-nginx
	Commands: systemctl status nginx
	systemctl enable nginx
	systelctl start --now nginx
	Once you edit the index.html page located in /var/www/html with your hello world page, you can configure Nginx to listen on port 8080 through these simple steps: https://ubuntu.com/tutorials/install-and-configure-nginx#1-overview

1. What other well-known service could be used instead of nginx? 
    > Your answer : Apache and Python

1. On your student machine, create a temporary http server with python, on port ``5000``. Then on your kali machine, open a browser and go to the address ``10.12.181.X:``.
    > Your command : python -m SimpleHTTPServer 5000 or python3 -m http.server 5000
	On the Kali machine, open a browser and type in: 10.12.1.33:5000
	The page renders the files on the directory the python command was initially ran on.

1. Let's imagine that a hacker owns the domain name ``g00gle.com``, which tool would allow him to obtain an ssl certificate (https) very easily?
    > Your answer : S/he can self sign a certificate by using openssl locally. Ref.: https://linuxconfig.org/how-to-generate-a-self-signed-ssl-certificate-on-linux
Alternatively, s/he could generate a free ssl certificate through https://www.sslforfree.com/ or https://zerossl.com/. The certificates generated are valid for 90 days. Then, it's just necessary to renew them. 

1. On a linux machine, what tool could you use to have a self-signed SSL certificate on your local machine (localhost) ? 
    > Your answer : openssl

1. On your student machine, install the ftp service and connect from your kali machine.
    > No answer required

1. What is the default port for ftp? 
    > Your answer : 21

1. Is the ftp protocol secured?
    > Your answer : No, it doesn't use any encryption. SFTP does.

1. On your student machine, install the telnet service and connect from your kali machine.
    > No answer required

1. What is the default port for telnet? 
    > Your answer : 23

1. Is the telnet protocol secured?
    > Your answer : No, it is an old protocol and the communication is not encrypted (plain text). SSH is secured, and therefore, widely used nowadays.
    
1. Create a share file with samba between your Kali machine and your student machine.
    > No answer required
---  
  # Downloading files
  ## Exercises 

1. On your Kali machine, create a file named malware.php.
    ````
    echo "This is a malware file" > malware.php
    ````
    Then, in the same directory, create a temporary server with python on port 5000.
    ````
    python3 -m http.server 5000
    ````
1. On your Student machine, download the malware.php file with the wget command.
    > Your command : I used my kali machine instead. wget http://10.12.1.33:5000/malware.php

1. On your Student machine, download the malware.php file with the cURL command.
    > Your command : I used my kali machine instead. curl -O http://10.12.1.33:5000/malware.php
  
1. On the student machine, create a file named password.txt and transfer it to your student machine with netcat
    > Your commands: 
	student: nc -lvp 4444 < passwd
	kali: nc 10.12.1.33 4444 > passwd

1. On the student machine,  transfer ``/etc/passwd`` file to your kali machine with tftp
    > your commands: tftp 10.12.1.33
	get /etc/passwd
The command above should work, but it doesn't.
  
 --End of file--
  
