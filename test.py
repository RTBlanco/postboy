# from postV2 import Tester, User, Notification
from postV2 import Tester, Notification

ronny = Tester('rtoribio','Ac44life#','phone0','ronny_node4')

push = Notification(UUID=ronny.uuid(), jsessionid=ronny.jsessionid(), device_type='FCM', k_lang='ENGLISH', l_lang='SPANISH')

push.send_daily()