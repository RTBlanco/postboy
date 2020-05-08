# from postV2 import Tester, User, Notification
from postV2 import Tester, Notification

ronny = Tester('username','password','acccount username ','node')

push = Notification(UUID=ronny.uuid(), jsessionid=ronny.jsessionid(), device_type='FCM', k_lang='ENGLISH', l_lang='SPANISH')

push.send_daily()
