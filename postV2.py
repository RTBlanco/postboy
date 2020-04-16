import requests, config


class Tester:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def jsessionid(self):
        """ uses the stick-e url to log to get the jsession id """
        payload = {'login':self.username, 'password':self.password}
        login_url = 'https://tlodockertest.transparent.local:7070/rest/admin/login'
        jsessionid = requests.Session().post(login_url, json=payload, verify=False).cookies.values()[0]
        return jsessionid

class User:
    def __init__(self, account_name, node_name):
        self.account_name = account_name
        self.node_name = node_name

    def uuid(self):
        """ will bring the correct UUID for the user """ 

        payload = {'login':config.username, 'password':config.password}
        # login_url = 'https://tlodockertest.transparent.local:7070/rest/admin/login'
        profile_search = f'https://tlodockertest.transparent.local:7070/rest/user/profile/{self.account_name}'

        search_request = requests.get(profile_search,headers={'Cookie':f'JSESSIONID={Tester.jsessionid()}'}, verify=False)
        uuid = [search_request.json()[lst].get('userUuid') for lst in range(len(search_request.json())) if search_request.json()[lst].get('nodeName') == 'test_ronny'][0]
        print(uuid)
    

class Notification:
    def __init__(self):
        pass        
    # def jsessionid(self):
    #     """ uses the stick-e url to log to get the jsession id """
    #     payload = {'login':self.username, 'password':self.password}
    #     login_url = 'https://tlodockertest.transparent.local:7070/rest/admin/login'
    #     jsessionid = requests.Session().post(login_url, json=payload, verify=False).cookies.values()[0]
    #     return jsessionid
        


    def send_daily(self, device_type):
        """ Posts the requests for daily refreshser """

        sticke_test_url = f'https://192.168.254.54:7070/rest/external/{config.userUid}/REFRESHER/{device_type}/{config.knownLanguage}/{config.learnedLanguage}'
        R = requests.post(sticke_test_url, headers={'Host':'notifications.transparent.com','Cookie':f'JSESSIONID={Tester.jsessionid()}'}, verify=False)

        print(R.status_code)
        print(R.text)



