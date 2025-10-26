#!/usr/bin/python3
"""2-recurse.py"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles.
        after (str): The 'after' key for pagination (defaults to None).

    Returns:
        list: List of titles of hot articles, or None if subreddit is invalid.
    """
    # Define the base URL and headers
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyRedditApp/0.1 (by u/yourusername)"}
    params = {"limit": 100, "after": after}  # Get up to 100 posts per call

    # Make the request to Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check for valid response
    if response.status_code != 200:
        return None

    # Extract the JSON data
    try:
        data = response.json().get("data", {})
        children = data.get("children", [])
        after = data.get("after", None)  # Pagination token

        # Add titles of hot posts to hot_list
        for post in children:
            hot_list.append(post.get("data", {}).get("title"))

        # If there's an 'after' value, make a recursive call to fetch more results
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    except (KeyError, ValueError):
        return None
