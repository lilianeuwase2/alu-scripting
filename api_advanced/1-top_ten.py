#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Prints:
        The titles of the top 10 hot posts, each on a new line.
        'None' if the subreddit is invalid or an error occurs.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    # Define the API endpoint and parameters
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 10}
    
    # Set a custom User-Agent to comply with Reddit's API rules
    # and avoid a 429 Too Many Requests error.
    headers = {'User-Agent': 'my-python-app/1.0 by u/gemini'}

    try:
        # Make the GET request, ensuring redirects are not followed
        response = requests.get(url,
                                headers=headers,
                                params=params,
                                allow_redirects=False)

        # If the status code is not 200 (OK), the subreddit is likely
        # invalid or another error occurred.
        if response.status_code != 200:
            print("None")
            return

        # Parse the JSON response
        data = response.json()

        # Safely navigate the JSON structure to get the list of posts
        posts = data.get('data', {}).get('children', [])

        if not posts:
            # If the 'children' list is empty or missing, print None
            print("None")
            return

        # Loop through the posts and print their titles
        for post in posts:
            title = post.get('data', {}).get('title')
            if title:
                print(title)

    except requests.RequestException:
        # Handle network-related errors (e.g., connection error)
        print("None")
    except (ValueError, AttributeError):
        # Handle errors from JSON decoding or unexpected data structure
        print("None")
