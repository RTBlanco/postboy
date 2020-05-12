from sticke.postV2 import Tester, Notification
# from post import Tester, Notification

ronny = Tester(username='TL username',password='TL password',account_name='user username',node_name=' node ',site=' LE,EE or GE test')

push = Notification(UUID=ronny.uuid(), jsessionid=ronny.jsessionid(), device_type='FCM', k_lang='ENGLISH', l_lang='SPANISH')

push.send_daily()
