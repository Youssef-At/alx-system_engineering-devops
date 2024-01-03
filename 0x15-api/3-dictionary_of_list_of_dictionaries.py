#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the JSON format.s
"""

import json
import requests

if __name__ == '__main__':
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    ).json()
    username_doc = {}
    user_doc = {}
    for user in users:
        UID = user.get("id")
        user_doc[UID] = []
        username_doc[UID] = user.get("username")
    url = "https://jsonplaceholder.typicode.com/todos"
    todo = requests.get(
        url,
    ).json()
    [
        user_doc.get(task.get("userId")).append(
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username_doc.get(task.get("userId"))
            }
        ) for task in todo
    ]
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(user_doc, jsonfile)
