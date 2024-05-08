#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """I'm the only function here"""
    url = "https://www.reddit.com/r/{sub}/hot.json".format(sub=subreddit)
    params = {"limit": 10}
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    res = requests.get(url=url, headers=headers, params=params)
    if res.status_code != 200:
        return print("None")
    data = res.json()["data"].get("children")
    if not data:
        return print("None")
    for post in data:
        print(post["data"].get("title"))
