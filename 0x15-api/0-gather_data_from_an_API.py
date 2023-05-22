import requests
import sys

if len(sys.argv) != 2 or not sys.argv[1].isdigit():
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = int(sys.argv[1])

# Make the API request
response_user = requests.get("https://jsonplaceholder.typicode.com/users/" + str(employee_id))
response_todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId=" + str(employee_id))

if response_user.status_code != 200 or response_todos.status_code != 200:
    print("Failed to retrieve data from the API.")
    sys.exit(1)

user_data = response_user.json()
todos_data = response_todos.json()

# Extract relevant information
employee_name = user_data["name"]
total_tasks = len(todos_data)
completed_tasks = sum(1 for todo in todos_data if todo["completed"])
completed_task_titles = [todo["title"] for todo in todos_data if todo["completed"]]

# Display the information
print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))
for title in completed_task_titles:
    print(" ", title)
