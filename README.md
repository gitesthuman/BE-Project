# BE-Project
Nike online shop based on Prestashop 8. Requires [Docker](https://www.docker.com/products/docker-desktop/) and Windows.

# Installation guide
```
docker-compose build
docker-compose up -d
```

# Managing
To stop the application use:
```
docker-compose stop
```
You can also start and stop application in Docker Desktop application.

---
At first, go to [phpMyAdmin](http://localhost:81) and import database `mariadb.sql`.


To enter the admin page, you need to enter `http://localhost:80/kupriano` and log in.

Email: `demo@prestashop.com`

Password: `dupaguwno` <sub>strong password ;)</sub>

# Enabling SSL

update apt

```
apt update
```
enable `mod_ssl`

```
a2enmod ssl
service apache2 reload
```

Create the SSL Certificate
```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```
Fill the form:
Country Name (2 letter code) [XX]:`pl`
State or Province Name (full name) []:`pomorskie`
Locality Name (eg, city) [Default City]:`gdansk` 
Organization Name (eg, company) [Default Company Ltd]:`pg`
Organizational Unit Name (eg, section) []:`biznes`
Common Name (eg, your name or your server's hostname) []:`Be-projekt`
Email Address []:`demo@prestashop.com`

Configure Apache to Use SSL

create file:
```
nano /etc/apache2/sites-available/html.conf
```

Paste in the following minimal VirtualHost configuration:
```
<VirtualHost *:443>
   ServerName localhost
   DocumentRoot /var/www/html

   SSLEngine on
   SSLCertificateFile /etc/ssl/certs/apache-selfsigned.crt
   SSLCertificateKeyFile /etc/ssl/private/apache-selfsigned.key
</VirtualHost>
```

save and close the file

type following:

```
a2ensite html.conf
apache2ctl configtest
```
ignore apache2 warning

if output gives: `Syntax OK` move on
```
service apache2 reload
```

Redirect HTTP to HTTPS
open previously created file

```
nano /etc/apache2/sites-available/html.conf
```
add following
```
<VirtualHost *:80>
    ServerName localhost
    Redirect / https://localhost/
</VirtualHost>
```
save and exit, then type

```
apachectl configtest
service apache2 reload
```
Done
