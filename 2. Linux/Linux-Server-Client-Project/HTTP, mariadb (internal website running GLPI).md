
Install apache2

Apache (HTTP) server:

`sudo apt install apache2


Install MariaDB (MySQL) server:

`sudo apt install mariadb-server`

Once MariaDB is installed, you can secure the installation by running the following command:

`sudo mysql_secure_installation`

Create a new account called **admin** with the same capabilities as the **root** account, but configured for password authentication. Open up the MariaDB prompt from your terminal:

`sudo mariadb`

`GRANT ALL ON *.* TO 'admin'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;

usr: admin
pass: mariaboss

Test it via the command: `sudo mysql -u admin -p`

![[Pasted image 20230614142431.png]]

Create a new database for GLPI. In the MariaDB shell, run the following commands:

`CREATE DATABASE glpidb;
`GRANT ALL PRIVILEGES ON glpidb.* TO 'glpiuser'@'localhost' IDENTIFIED BY 'glpiboss';
`FLUSH PRIVILEGES;
`EXIT;

Install PHP and necessary modules:

`sudo apt install php libapache2-mod-php php-mysql -y

Restart Apache for the changes to take effect:

`sudo systemctl restart apache2`

### Firewall

sudo ufw allow 80 
sudo ufw allow 443

### Installing GLPI

Installing GLPI on Ubunutu:

The easiest way is to follow this video: 
https://www.youtube.com/watch?v=X3jbo6rFntI&t=458s

Or, follow this tutorial:
https://unixcop.com/how-to-install-glpi-on-ubuntu-22-04/

Download link:
`cd /tmp/ wget https://github.com/glpi-project/glpi/releases/download/10.0.7/glpi-10.0.7.tgz


![[Pasted image 20230615105519.png]]

Change the passwords of the accounts above.