import module

module.greeting("salman")

print(module.add(2,5))
print(module.sub(5,2))

print(module.test)

print(module.person)
print(module.person["name"])





import module as m

print(m.person['name'])





from module import greeting , person , add 

greeting("M.Suleman")

print(person['name'])

print(add(23,54))








from module import *

print(person['name'])

print(add(23,54))