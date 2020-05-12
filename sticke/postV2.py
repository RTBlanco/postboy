import requests
from json import JSONDecodeError

class Tester:
    def __init__(self, username, password, account_name, node_name, site):
        self.username = username
        self.password = password
        self.account_name = account_name
        self.node_name = node_name
        self.site = site

    def jsessionid(self):
        """ uses the stick-e url to log to get the jsession id """
        payload = {'login':self.username, 'password':self.password}
        login_url = """ TL link """
        try:
            jsessionid = requests.Session().post(login_url, json=payload, verify=False).cookies.values()[0]
            return jsessionid
        except IndexError as error:
            print(f'{error}: TL username or password incorrect')

    def uuid(self):
        """ will bring the correct UUID for the user """ 

        profile_search = f'""" TL link """{self.account_name}'
        search_request = requests.get(profile_search,headers={'Cookie':f'JSESSIONID={self.jsessionid()}'}, verify=False)
        try:
            uuid = [search_request.json()[lst].get('userUuid') for lst in range(len(search_request.json())) if search_request.json()[lst].get('nodeName') == self.node_name and search_request.json()[lst].get('srvName') == self.site ][0]
            return uuid
        except JSONDecodeError as error:
            print(f'{error}: incorrect node user information')
        except IndexError as error: 
            print(f'{error}: incorrect node user information')



class Notification:
    def __init__(self, UUID, jsessionid, device_type, k_lang, l_lang):
        self.UUID = UUID
        self.jsessionid = jsessionid
        self.device_type = device_type
        self.k_lang = k_lang
        self.l_lang = l_lang

    def send_daily(self):
        """ Posts the requests for daily refreshser """

        sticke_test_url = f'""" TL link """{self.UUID}""" TL link """{self.device_type}/{self.k_lang}/{self.l_lang}'
        R = requests.post(sticke_test_url, headers={'Host':'notifications.transparent.com','Cookie':f'JSESSIONID={self.jsessionid}'}, verify=False)

        print(R.status_code)
        print(R.text)



