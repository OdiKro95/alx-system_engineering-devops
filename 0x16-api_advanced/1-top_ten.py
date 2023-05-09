import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyBot/0.0.1"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()["data"]["children"]
        for post in data:
            print(post["data"]["title"])
    else:
        print(None)
