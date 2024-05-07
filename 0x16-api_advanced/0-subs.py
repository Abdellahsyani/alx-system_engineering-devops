#!/usr/bin/python3
"""get the number of subs"""
import requests


def number_of_subscribers(subreddit):
    """Get the number of subs to a subreddit"""
    url = "https://www.reddit.com/r/{sub}/about.json"
    headers = {
            "User-Agent": "abdellah:intranet",
    }
    res = requests.get(url=url.format(sub=subreddit), headers=headers)
    if res.status_code != 200:
        return 0
    data = res.json()["data"]
    return data.get("subscribers", 0)
