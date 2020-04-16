import requests
import config

# custom_header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
#     'Accept':'application/json, text/plain, */*',
#     'Sec-Fetch-Dest': 'empty',
#     'Content-Type': 'application/json;charset=UTF-8',
#     'Origin':'https://tlodockertest.transparent.local:7070',
#     'Sec-Fetch-Site':'same-origin',
#     'Sec-Fetch-Mode':'cors',
#     'Referer':'https://tlodockertest.transparent.local:7070/qa/',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'en-US,en;q=0.9,es;q=0.8,fr;q=0.7,pt;q=0.6,sv;q=0.5,el;q=0.4'
#     } 


login_url = 'https://tlodockertest.transparent.local:7070/rest/admin/login'
payload = {'login':config.username, 'password':config.password}
jsessionid = requests.Session().post(login_url, json=payload, verify=False).cookies.values()[0]


# with requests.Session() as session:
#     # post = session.post(login_url, json=payload, headers=custom_header, verify=False)
#     post = session.post(login_url, json=payload, verify=False)
#     cookie = post.cookies.values()[0]

# post = session.post(login_url, json=payload, verify=False).cookies.values()[0]
# cookie = post.cookies.values()[0] 