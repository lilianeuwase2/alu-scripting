#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a given subreddit."""

import requests


def top_ten(subreddit):
    """
    Query the Reddit API and print the titles of the first 10 hot posts.

    Args:
        subreddit (str): The subreddit to query.

    Prints:
        The titles of the first 10 hot posts, or None if the subreddit is invalid.
    """
    if not isinstance(subreddit, str) or not subreddit:
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "ALU-Reddit-Task/0.1"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            print(None)
            return
        
        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print(None)
            return

        for post in posts[:10]:
            print(post.get("data", {}).get("title"))

    except requests.exceptions.RequestException:
        print(None)
