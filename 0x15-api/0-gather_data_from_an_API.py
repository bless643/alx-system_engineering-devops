#!/usr/bin/python3

"""
0-gather_data_from_an_API.py
---------------------------
Python script to fetch TODO list progress for a given employee ID from a REST API.

Requirements:
- Uses urllib or requests module
- Accepts an integer as a parameter (employee ID)
- Displays employee TODO list progress in a specific format
- Organizes libraries in alphabetical order
- Follows PEP 8 style guidelines
- Does not execute code when imported

"""

import requests
from sys import argv


def fetch_data(employee_id):
    """
    Fetches TODO list progress for a given employee ID from the API.

    Args:
        employee_id (int): The employee ID.

    Returns:
        None

    """

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    if user_response.status_code != 200:
        print(f"Error: Could not fetch user data for employee ID {employee_id}")
        return

    if todo_response.status_code != 200:
        print(f"Error: Could not fetch todo data for employee ID {employee_id}")
        return

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data.get("name")
    tasks_completed = sum(1 for task in todo_data if task.get("completed"))

    total_tasks = len(todo_data)
    task_titles = [task.get("title") for task in todo_data if task.get("completed")]

    print(f"Employee {employee_name} is done with tasks ({tasks_completed}/{total_tasks}):")
    for title in task_titles:
        print("\t", title)


if __name__ == "__main__":
    """
    Main entry point of the script.
    """

    if len(argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        employee_id = int(argv[1])
        fetch_data(employee_id)
