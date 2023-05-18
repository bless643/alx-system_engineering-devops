# MySQL

## Project Structure

- `README.md`: This file, providing an overview of the project.
- `install_mysql.sh`: Bash script for installing MySQL.
- `configure_mysql.sh`: Bash script for configuring MySQL.

## Installation

To install MySQL on the servers, follow these steps:

```bash
sudo apt install mysql-client-core-8.0     # version 8.0.30-0ubuntu0.20.04.2, or
sudo apt install mariadb-client-core-10.3  # version 1:10.3.34-0ubuntu0.20.04.1
Verify the installation by running mysql --version on each server. The output should indicate the installed MySQL version.

Usage
Once MySQL is installed, you can perform various tasks such as:

Accessing the MySQL command line interface: mysql -u <username> -p
Managing databases and tables: Use MySQL commands like CREATE DATABASE, CREATE TABLE, INSERT INTO, etc.
Configuring MySQL settings: Refer to the MySQL documentation for details.
Testing
To verify the successful installation of MySQL, perform the following tests:

Connect to the MySQL server using mysql -u <username> -p.
Create a new database and table.
Insert data into the table.
Retrieve and verify the data using SQL queries.
Troubleshooting
If you encounter any issues during installation or configuration, consider the following troubleshooting steps:

Ensure you have the necessary privileges.
Double-check the commands used for installation.
Search for error messages online or consult the MySQL documentation for troubleshooting guidance.
Author
Samuel Ojo
