import requests

def get_Reddit():
    base_url = r'https://www.reddit.com/'
    data = {'grant_type': 'password' , 'username': REDDIT-USERNAME, 'password': REDDIT-PASSWORD}
    auth = requests.auth.HTTPBasicAuth(APP-ID, APP-SECRET)
    r = requests.post(base_url + 'api/v1/access_token', data=data, headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'}, auth=auth)
    status = r.status_code

requests.get(base_url)
print(status)

if r.status_code==401:
    print("401 Unauthorized Request!")
elif r.status_code==404:
    print("404 Request not found!")
else:
    print("200 OK!")
