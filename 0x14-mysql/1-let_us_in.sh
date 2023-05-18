#!/usr/bin/env bash

# Create MySQL user on web-01
mysql -e "CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';"
mysql -e "GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';"

# Create MySQL user on web-02
ssh ubuntu@52.3.246.108 "mysql -e \"CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';\""
ssh ubuntu@52.3.246.108" "mysql -e \"CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';\""

