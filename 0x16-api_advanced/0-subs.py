#!/usr/bin/python3
"""
This script retrieves the number of subscribers from Reddit API.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Retrieves the total number of subscribers for a specified subreddit.
    """
    # Define the base URL
    base_url = 'https://www.reddit.com'
    
    # Construct the API URI
    api_uri = '{base}/r/{subreddit}/about.json'.format(base=base_url,
                                                       subreddit=subreddit)
    
    # Set the User-Agent
    user_agent = {'User-Agent': 'Python/requests'}
    
    # Send a GET request to the Reddit API
    response = requests.get(api_uri, headers=user_agent, allow_redirects=False)
    
    # Check if the subreddit is invalid
    if response.status_code in [302, 404]:
        return 0
    
    # Retrieve the total subscribers count from the response
    total_subscribers = response.json().get('data', {}).get('subscribers', 0)
    
    return total_subscribers
