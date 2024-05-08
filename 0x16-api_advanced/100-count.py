#!/usr/bin/python3
"""get a list of the titles of posts listed for a given subreddit"""
import requests


def get_posts(subreddit, after=""):
    """I'm the only function here"""
    url = "https://www.reddit.com/r/{sub}/hot.json".format(sub=subreddit)
    params = {"limit": 100, "after": after}
    headers = {
        "User-Agent": "abdellah:intranet.alxswe.com:v2.4.1 (by /u/keroxyz)",
    }
    res = requests.get(url=url, headers=headers, params=params)
    if res.status_code != 200:
        return None, None
    data = res.json()["data"].get("children")
    if not data:
        return None, None
    return data, res.json()["data"].get("after")
