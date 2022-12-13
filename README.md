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

```
apt update
```
Enable `mod_ssl`

```
a2enmod ssl
service apache2 reload
```

Create the SSL Certificate
```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```
Fill the form:<br />
Country Name (2 letter code) [XX]:`pl`<br />
State or Province Name (full name) []:`pomorskie`<br />
Locality Name (eg, city) [Default City]:`gdansk` <br />
Organization Name (eg, company) [Default Company Ltd]:`pg`<br />
Organizational Unit Name (eg, section) []:`biznes`<br />
Common Name (eg, your name or your server's hostname) []:`Be-projekt`<br />
Email Address []:`demo@prestashop.com`<br />

Configure Apache to Use SSL

Create file:
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

Save and close the file. Type following:

```
a2ensite html.conf
apache2ctl configtest
```
Ignore apache2 warning. If `output` gives: `Syntax OK` move on:
```
service apache2 reload
```

Redirect HTTP to HTTPS<br />
Open previously created file:

```
nano /etc/apache2/sites-available/html.conf
```
Add following:
```
<VirtualHost *:80>
    ServerName localhost
    Redirect / https://localhost/
</VirtualHost>
```
Save and exit, then type:

```
apachectl configtest
service apache2 reload
```
Done
