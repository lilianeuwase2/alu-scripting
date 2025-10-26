#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
and prints the top 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit.

    If the subreddit is not valid or an error occurs, prints "None".

    Args:
        subreddit (str): The subreddit name to query.
    """
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    # Set a custom User-Agent as required by Reddit API rules to avoid 429 errors
    user_agent = 'python:1-top_ten:v1.0 (by /u/gemini_bot)'
    headers = {'User-Agent': user_agent}
    
    # Set parameters for the request: limit to 10 posts
    params = {'limit': 10}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    try:
        # Make the GET request, disallowing redirects
        # allow_redirects=False ensures that we don't follow a redirect
        # to a search page for an invalid subreddit.
        response = requests.get(url,
                                headers=headers,
                                params=params,
                                allow_redirects=False)

        # If status code is not 200 (OK), it's an invalid subreddit
        # (e.g., 404 Not Found) or another error.
        if response.status_code != 200:
            print("None")
            return

        # Parse the JSON response
        data = response.json()

        # Safely extract the list of posts ('children')
        posts = data.get('data', {}).get('children', [])

        # If 'posts' is empty (a valid subreddit with no posts),
        # this loop will simply not run, and nothing will be printed,
        # which is the correct behavior.
        for post in posts:
            title = post.get('data', {}).get('title')
            if title:
                print(title)

    except (requests.RequestException, ValueError, AttributeError):
        # Catch potential network errors, JSON decode errors, or
        # errors from an unexpected data structure.
        print("None")

