#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit
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

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}

    # Avoid redirects as required
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        data = response.json().get("data", {}).get("children", [])
        if not data:
            print("None")
            return

        for post in data[:10]:
            print(post.get("data", {}).get("title"))
    except Exception:
        print("None")
