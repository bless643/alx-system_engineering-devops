#!/usr/bin/env bash

# Create database and table on web-01
mysql -e "CREATE DATABASE tyrell_corp;"
mysql -e "USE tyrell_corp; CREATE TABLE nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));"
mysql -e "USE tyrell_corp; INSERT INTO nexus6 (name) VALUES ('Leon');"
mysql -e "GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';"

# Check if the table exists and is not empty on web-01
mysql -e "USE tyrell_corp; SELECT * FROM nexus6;"

# Check if the table exists and is not empty on web-02
ssh ubuntu@52.3.246.108"mysql -e \"USE tyrell_corp; SELECT * FROM nexus6;\""
