#!/usr/bin/python3
"""exporting data gathered from an API to csv"""
import csv
import requests
import sys

if __name__ == '__main__':
    
    user_id = sys.argv[1]

    url_users = requests.get("https://jsonplaceholder.typicode.com")


