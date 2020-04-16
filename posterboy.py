import requests, config, Jsession


#headers = {'Cookie':f'JSESSIONID={config.cookie}'}
headers = {
    'Host':'notifications.transparent.com',
    'Cookie':f'JSESSIONID={Jsession.jsessionid}'
    }

sticke_test_url = f'https://192.168.254.54:7070/rest/external/{config.userUid}/REFRESHER/APN/{config.knownLanguage}/{config.learnedLanguage}'
# sticke_test_url = f'https://notifications.transparent.com/rest/external/{config.userUid}/REFRESHER/FCM/{config.knownLanguage}/{config.learnedLanguage}?'

R = requests.post(sticke_test_url, headers=headers, verify=False)

print(R.status_code)
print(R.text)
