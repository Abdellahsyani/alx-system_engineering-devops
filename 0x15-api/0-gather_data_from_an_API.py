#!/usr/bin/python3
"""get data from APIs """
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        user = requests.get('https://jsonplaceholder.typicode.com'
                            '/users?name' + sys.argv[1])
        user = user.json()
        tasks = requests.get('https://jsonplaceholder.typicode.com'
                             '/todos?userId=' + sys.argv[1])
        tasks = tasks.json()
        uncompleted = [t.get('title') for t in tasks if t.get('completed')]
        print('Employee {} is done with tasks({}/{}):'
              .format(user[0].get('name'), len(uncompleted), len(tasks)))
        for task in uncompleted:
            print('\t ' + str(task))
