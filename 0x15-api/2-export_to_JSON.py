#!/usr/bin/python3
'''
Python script to export data in the JSON format.
'''

import json
import requests
from sys import argv

if __name__ == '__main__':
    UID = argv[1]
    Link = "https://jsonplaceholder.typicode.com/users/{}".format(
        UID
    )
    user = requests.get(
        Link,
    ).json()
    Link = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        UID
    )
    RequestData = requests.get(
        Link,
    ).json()
    username = user.get('username')
    tasks = []
    for task in RequestData:
        tasks.append(
            {
                "task": task.get("title"),
                "username": username,
                "completed": task.get("completed")
            }
        )
    jsonOBJ = {}
    jsonOBJ[UID] = tasks
    with open("{}.json".format(UID), 'w') as jsonfile:
        json.dump(jsonOBJ, jsonfile)
