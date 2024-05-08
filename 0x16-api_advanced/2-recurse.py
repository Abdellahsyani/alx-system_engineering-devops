#!/usr/bin/python3
"""get a list of the titles of posts listed for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """I'm the only function here"""
    url = "https://www.reddit.com/r/{sub}/hot.json".format(sub=subreddit)
    params = {"limit": 100, "after": after}
    headers = {
        "User-Agent": "abdellah:intranet.alxswe.com:v2.4.1 (by /u/keroxyz)",
    }
    res = requests.get(url=url, headers=headers, params=params)
    if res.status_code != 200:
        return None
    data = res.json()["data"].get("children")
    if not data:
        return None
    for post in data:
        hot_list.append(post["data"].get("title"))
    after = res.json()["data"].get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
