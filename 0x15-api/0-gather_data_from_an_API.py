#!/usr/bin/python3
"""import data from API
"""

from json import loads
from requests import get
from sys import argv
if __name__ == "__main__":

    employee_id = argv[1]
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos/"\
        .format(employee_id)
    user_url = "https://jsonplaceholder.typicode.com/users/{}"\
        .format(employee_id)

    response_todo = get(todo_url)
    response_user = get(user_url)

    list_emp = response_todo.json()
    EMPLOYEE_NAME = response_user.json().get('name')
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = len(list_emp)
    for i in list_emp:
        if i.get('completed'):
            NUMBER_OF_DONE_TASKS += 1

    print(f"Employee {EMPLOYEE_NAME} is done with tasks", end="")
    print(f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    for i in list_emp:
        if i.get('completed'):
            print("\t {}".format(i.get('title')))
