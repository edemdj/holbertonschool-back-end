#!/usr/bin/python3
import requests
import json
import sys

def export_to_json(user_id, username, tasks):
    data = {str(user_id): [{"task": task["title"], "completed": task["completed"], "username": username} for task in tasks]}
    json_output = json.dumps(data, indent=4)
    print(json_output)

def get_employee_todo_progress(employee_id):
    root = "https://jsonplaceholder.typicode.com"
    users = requests.get(root + "/users", params={"id": employee_id})
    
    if users.status_code == 200:
        for user in users.json():
            user_id = user['id']
            username = user['name']
            
            todos = requests.get(root + "/todos", params={"userId": user_id})
            if todos.status_code == 200:
                tasks = todos.json()
                export_to_json(user_id, username, tasks)
            else:
                print(f"Failed to fetch tasks for user {username}.")
    else:
        print("Failed to fetch user information.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py employee_id")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
