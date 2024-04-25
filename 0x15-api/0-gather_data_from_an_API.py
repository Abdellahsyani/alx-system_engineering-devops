#!/usr/bin/python3
"""import data from API
"""
import requests
import sys

if __name__ == "__main__":
    url_user = requests.get("https://jsonplaceholder.typicode.com/users?id="
                            + sys.argv[1])
    url_todo = requests.get("https://jsonplaceholder.typicode.com"
                            "/todos?userId=" + sys.argv[1])


    user = url_user.json()
    todo = url_todo.json()

    EMPLOYEE_NAME = user[0].get('name')
    NUMBER_OF_DONE_TASKS = sum(1 for i in todo if i.get('completed'))
    TOTAL_NUMBER_OF_TASKS = len(todo)

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS,
                  TOTAL_NUMBER_OF_TASKS))
    for i in todo:
        if i.get('completed'):
            print("\t {}".format(i.get('title')))
