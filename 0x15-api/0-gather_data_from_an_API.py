#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

This script gathers information about an employee's TODO list progress from an API.

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


def gather_data(employee_id):
    """
    Gathers and displays information about an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee
    """

    # Get user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        username = user_data.get("name")

        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        total_tasks = len(todo_data)
        completed_tasks = [task for task in todo_data if task.get("completed")]
        num_completed_tasks = len(completed_tasks)

        # Display employee information
        print(f"Employee {username} is done with tasks({num_completed_tasks}/{total_tasks}):")

        # Display completed task titles
        for task in completed_tasks:
            print("\t" + task.get("title"))

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Ensure the employee ID is an integer
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    gather_data(employee_id)
