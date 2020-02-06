import requests
import praw

def get_Reddit():
    base_url = r'https://www.reddit.com/'
    data = {'grant_type': 'password' , 'username': REDDIT-USERNAME, 'password': REDDIT-PASSWORD}
    auth = requests.auth.HTTPBasicAuth(APP-ID, APP-SECRET)
    r = requests.post(base_url + 'api/v1/access_token', data=data, headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'}, auth=auth)
    status = r.status_code

requests.get(base_url)
print(status)

# credentials
with open('credentials.json', 'r') as f:
    credentials = json.load(f)

# create reddit wrapper api
reddit = praw.Reddit(client_id=credentials['client_id'],
                     client_secret=credentials['client_secret'],
                     user_agent='my user agent')

for submission in reddit.subreddit('news').hot(limit=10): #testing if I have authorization to scrape
    print(submission.title)
    print("----------------")

