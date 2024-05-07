#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """Retrieve the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Make the API request
    response = requests.get(url)

    # Check if the response status code indicates success (200 OK)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract the number of subscribers
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        # If the subreddit is not found, return 0
        return 0
