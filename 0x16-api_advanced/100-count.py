import requests

def count_words(subreddit, word_list, word_count={}):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        if response.status_code == 302:
            print("Subreddit doesn't exist")
        return
    
    data = response.json()['data']['children']
    for post in data:
        title = post['data']['title'].lower()
        for word in word_list:
            if ' ' in word:
                continue
            if word.lower() in title:
                word_count[word] = word_count.get(word, 0) + 1
    
    if len(data) == 0:
        for word, count in sorted(word_count.items(), key=lambda x: (-x[1], x[0])):
            print(word + ': ' + str(count))
        return
    
    last_post = data[-1]['data']['name']
    count_words(subreddit, word_list, word_count)
    
    new_response = requests.get(url, headers=headers, params={'after': last_post}, allow_redirects=False)
    if new_response.status_code == 200:
        count_words(subreddit, word_list, word_count)
    else:
        print("An error occurred while fetching the next page of posts")
