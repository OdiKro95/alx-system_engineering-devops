import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "my-bot/0.0.1"}

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None

    data = response.json()
    children = data.get("data", {}).get("children", [])
    for child in children:
        hot_list.append(child["data"]["title"])

    if data.get("data", {}).get("after"):
        recurse(subreddit, hot_list, data["data"]["after"])

    return hot_list[:10]
