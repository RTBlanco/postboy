from postV2 import Tester, User, Notification


ronny = Tester('rtoribio','Ac44life#')

phone = User('phone0','ronny_node4')

# uuid = sponge_bob.uuid(ronny.jsessionid())

# print(uuid)

# push = Notification(uuid, ronny.jsessionid())


j_id = ronny.jsessionid()

uuid = phone.uuid(j_id)

push = Notification(uuid, j_id)

push.send_daily('FCM','ENGLISH','SPANISH')