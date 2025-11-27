from pack.User import User
from pack.Guild import Guild

a = User('탱커')
a.setLevel(30)
a.addInven('방패')
a.addInven('칼')
print(1, a)
print(2, str(a) + "!!!!!")

b = User('힐러')
b.setLevel(20)
b.addInven('물약_HP')
b.addInven('주문서')
b.addInven('물약_MP')

c = User('딜러')
c.setLevel(10)
c.addInven('단검')

g = Guild('파이썬팟')
g.addUser(a)
g.addUser(b)
g.addUser(c)

print(g.getRanker())
print(g.getBestSales())
print(g.getUsers())

print(g)
