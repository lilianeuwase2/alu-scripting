#!/usr/bin/python3
"""
Print the titles of the first 10 Hot Posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit. Prints None if the subreddit is invalid.
    """
    # Set a custom User-Agent to avoid 429 Too Many Requests errors
    headers = {'User-Agent': 'python:my_reddit_script:v1.0.0 (by anonymous)'}

    # Use the correct API endpoint for /hot posts
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set parameters to limit the number of posts to 10
    params = {'limit': 10}

    # Add allow_redirects=False.
    # This ensures that if the subreddit is non-existent,
    # we get a 404 or 302 status, not a 200 status from a redirect.
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Parse the JSON response
            json_data = response.json()
            
            # Safely get the list of 'children' (posts)
            children = json_data.get('data', {}).get('children', [])

            if not children:
                # Subreddit is valid but has no posts
                print(None)
                return

            # Iterate through the returned posts and print their titles
            for post in children:
                print(post.get('data', {}).get('title'))

        except (ValueError, AttributeError):
            # Handle cases where JSON is malformed or structure is unexpected
            print(None)
    else:
        # If status code is not 200 (e.g., 404 for invalid subreddit)
        print(None)
