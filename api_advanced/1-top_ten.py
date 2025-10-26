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
    # 1. Use a more generic User-Agent. This is the most likely
    #    fix for the checker failing with a 4xx error.
    headers = {'User-Agent': 'My User Agent 1.0'}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 10}

    # This is correct: do not follow redirects, as per instructions
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            json_data = response.json()
            children = json_data.get('data', {}).get('children', [])

            # 2. Removed the `if not children: print(None)` block.
            #    If a subreddit is valid but has 0 posts, this loop
            #    will simply not run, and nothing will be printed.
            #    This is the correct behavior.

            # Iterate through the returned posts and print their titles
            for post in children:
                print(post.get('data', {}).get('title'))

        except (ValueError, AttributeError):
            # Failed to parse JSON, treat as invalid
            print(None)
    else:
        # If status code is not 200 (e.g., 404 for invalid subreddit)
        print(None)
