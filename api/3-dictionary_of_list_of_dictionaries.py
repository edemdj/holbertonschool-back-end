#!/usr/bin/python3
import requests
import json

def export_to_json(data):
    filename = "todo_all_employees.json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def get_all_employee_todo_progress():
    root = "https://jsonplaceholder.typicode.com"
    users = requests.get(root + "/users")

    if users.status_code == 200:
        all_tasks = {}
        for user in users.json():
            user_id = user['id']
            username = user['name']
            
            todos = requests.get(root + "/todos", params={"userId": user_id})
            if todos.status_code == 200:
                tasks = todos.json()
                for task in tasks:
                    task_data = {"username": username, "task": task["title"], "completed": task["completed"]}
                    if user_id in all_tasks:
                        all_tasks[user_id].append(task_data)
                    else:
                        all_tasks[user_id] = [task_data]
            else:
                print(f"Failed to fetch tasks for user {username}.")
        
        export_to_json(all_tasks)
    else:
        print("Failed to fetch user information.")

if __name__ == "__main__":
    get_all_employee_todo_progress()
