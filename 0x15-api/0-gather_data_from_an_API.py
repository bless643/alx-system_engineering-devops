#!/usr/bin/python3

"""
0-gather_data_from_an_API.py
Description: This script gathers information about an employee's TODO list progress from an API.

Usage: python3 0-gather_data_from_an_API.py <employee_id>

Arguments:
    <employee_id>: An integer representing the ID of the employee

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


def retrieve_employee_data(employee_id):
    """
    Retrieve employee data from the API

    Args:
        employee_id (int): The ID of the employee

    Returns:
        tuple: A tuple containing the user data and the TODO list data
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user_url, verify=False)
    todos_response = requests.get(todos_url, verify=False)

    if user_response.status_code != 200:
        print(f"Error: Unable to retrieve user data for employee ID {employee_id}")
        sys.exit(1)

    if todos_response.status_code != 200:
        print(f"Error: Unable to retrieve TODO list data for employee ID {employee_id}")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data


def display_todo_list_progress(user_data, todos_data):
    """
    Display the employee's TODO list progress

    Args:
        user_data (dict): User data retrieved from the API
        todos_data (list): TODO list data retrieved from the API
    """
    employee_name = user_data.get("name")
    total_tasks = len(todos_data)
    done_tasks = sum(1 for todo in todos_data if todo.get("completed"))

    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for todo in todos_data:
        if todo.get("completed"):
            print("\t", todo.get("title"))


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_data, todos_data = retrieve_employee_data(employee_id)
    display_todo_list_progress(user_data, todos_data)
