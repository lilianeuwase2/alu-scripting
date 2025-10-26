#!/usr/bin/python3
"""
A module that queries the Reddit API and prints the titles of the first
10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Prints:
        The titles of the first 10 hot posts, each on a new line.
        'None' if the subreddit is invalid or an error occurs.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    # Set a custom, unique User-Agent to avoid API errors
    headers = {'User-Agent': 'my-python-app/1.0.1'}

    # Set the parameters for the query
    params = {'limit': 10}

    # Construct the URL using .format() for compatibility with Python 3.4
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    try:
        # Make the GET request
        # allow_redirects=False is crucial to detect invalid subreddits
        response = requests.get(url,
                                headers=headers,
                                params=params,
                                allow_redirects=False)

        # If the status code is not 200 (OK), it's an invalid subreddit
        # or another error (e.g., 404 Not Found, 302 Found/Redirect)
        if response.status_code != 200:
            print("None")
            return

        # Parse the JSON response
        data = response.json()

        # Check for the expected data structure
        if 'data' not in data or 'children' not in data.get('data'):
            print("None")
            return

        # Get the list of posts
        children = data.get('data').get('children')

        if not children:
            # Valid subreddit, but no posts. Print nothing.
            return

        # Loop through the posts and print the title
        for post in children:
            # Safely get the title from the post data
            title = post.get('data', {}).get('title')
            if title:
                print(title)

    except (requests.exceptions.RequestException,
            KeyError,
            AttributeError,
            ValueError):
        # Catch all potential errors (network, JSON parsing, bad structure)
        print("None")
