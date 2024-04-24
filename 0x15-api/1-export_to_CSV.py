#!/usr/bin/python3
"""exporting data gathered from an API to csv"""
import csv
import requests
import sys

if __name__ == '__main__' and len(sys.argv) > 1:
    id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/' + id)
    user = user.json()
    if not user.get('name'):
        exit()
    name = user.get('username')
    tasks = requests.get('https://jsonplaceholder.typicode.com'
                         '/todos?userId=' + id)
    tasks = tasks.json()
    with open(id + '.csv', 'w', newline='') as file:
        writer = csv.writer(file,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([id,
                             name,
                             task.get('completed'),
                             task.get('title')])
