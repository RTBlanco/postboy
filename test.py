from postV2 import Tester, User, Notification


ronny = Tester('rtoribio','Ac44life#')

sponge_bob = User('sponge_bob','ronny_node')

# uuid = sponge_bob.uuid(ronny.jsessionid())

# print(uuid)

# push = Notification(uuid, ronny.jsessionid())


j_id = ronny.jsessionid()

uuid = sponge_bob.uuid(j_id)

push = Notification(uuid, j_id)

push.send_daily('APN','ENGLISH','SPANISH')