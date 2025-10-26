#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:alx.api_advanced:v1.0 (by /u/fake_user)"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False, timeout=10
        )

        if response.status_code != 200:
            print("None")
            return

        data = response.json().get("data", {}).get("children", [])
        if not data:
            print("None")
            return

        for post in data:
            print(post.get("data", {}).get("title"))

    except Exception:
        print("None")
