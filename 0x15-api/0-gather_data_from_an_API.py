#!/usr/bin/python3
'''
Python script that, using this REST API,
for a given employee ID, returns
information about his/her RequestData list progress.
'''
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
    with open("{}.csv".format(user_id), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in RequestData:
            taskwriter.writerow(
                [
                    int(user_id),
                    user.get('username'),
                    task.get('completed'),
                    task.get('title')
                ]
            )
