#!/usr/bin/python3

"""
0-gather_data_from_an_API.py
Description: This script gathers information about an employee's TODO list progress from an API.

Usage: python3 0-gather_data_from_an_API.py <employee_id>

Arguments:
    <employee_id>: An integer representing the ID of the employee

The script makes API requests to retrieve user and TODO list data for the specified employee ID. It then extracts the relevant information and displays the progress of completed tasks.

Dependencies:
    - requests module

API endpoints used:
    - User data: https://jsonplaceholder.typicode.com/users/<employee_id>
    - TODO list data: https://jsonplaceholder.typicode.com/todos?userId=<employee_id>
"""

import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if len(sys.argv) != 2 or not sys.argv[1].isdigit():
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = int(sys.argv[1])

# Make the API request
response_user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}", verify=False)
response_todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}", verify=False)

# Check if the API requests were successful
if response_user.status_code != 200:
    print(f"Error: Unable to retrieve user data for employee ID {employee_id}")
    sys.exit(1)

if response_todos.status_code != 200:
    print(f"Error: Unable to retrieve TODO list data for employee ID {employee_id}")
    sys.exit(1)

# Extract relevant information from the API responses
user_data = response_user.json()
todos_data = response_todos.json()

# Get user details
employee_name = user_data.get("name")
employee_username = user_data.get("username")

# Get TODO list progress
total_tasks = len(todos_data)
done_tasks = sum(1 for todo in todos_data if todo.get("completed"))

# Display the TODO list progress
print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
for todo in todos_data:
    if todo.get("completed"):
        print("\t", todo.get("title"))
