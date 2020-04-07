import requests, config, get_jid


headers = {'Cookie':f'JSESSIONID={get_jid.cookie}'}

sticke_test_url = f'https://192.168.254.54:7070/rest/external/{config.userUid}/REFRESHER/APN/{config.knownLanguage}/{config.learnedLanguage}'

R = requests.post(sticke_test_url, headers=headers, verify=False)

print(R.text)