#!/usr/bin/python3
import csv
import requests
import sys

def export_to_csv(user_id, username, tasks):
    filename = f"{user_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for task in tasks:
            writer.writerow({'USER_ID': user_id, 'USERNAME': username, 'TASK_COMPLETED_STATUS': task['completed'], 'TASK_TITLE': task['title']})

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
                export_to_csv(user_id, username, tasks)
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
