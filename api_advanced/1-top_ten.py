#!/usr/bin/python3
"""Prints titles of the first 10 hot posts for a given subreddit"""
import requests


def top_ten(subreddit):
    """Queries Reddit API"""
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "linux:api_advanced:v1.0 (by /u/yourusername)"}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        print("None")
        return

    data = r.json().get("data", {}).get("children", [])
    if not data:
        print("None")
        return

    for post in data:
        print(post.get("data", {}).get("title"))
