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