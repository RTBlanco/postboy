#TODO: Get the users UUID by just entering username and node 

import requests, config, Jsession

payload = {'login':config.username, 'password':config.password}
login_url = 'https://tlodockertest.transparent.local:7070/rest/admin/login'
new_url = 'https://tlodockertest.transparent.local:7070/rest/user/profile/wolverine'

new_post = requests.get(new_url,headers={'Cookie':f'JSESSIONID={Jsession.jsessionid}'}, verify=False)
uuid = [new_post.json()[lst].get('userUuid') for lst in range(len(new_post.json())) if new_post.json()[lst].get('nodeName') == 'test_ronny'][0]
print(uuid)