# birthday = '1/6/1952'
# print(birthday.split('/'))

small_birds = ['hummingbird','finch']

extinct_birds = ['dodo','passenger pigeon','Norwegian Blue']

carol_birds = [3,'French hens',2,'turtledov']

all_birds = [small_birds,extinct_birds,'macaw',carol_birds]

print(all_birds)

##########################

marxes = ['Groucho','Chico','Harpo']

print(marxes[0:2]+'\n')

print(marxes[::2]+'\n')

print(marxes[::-2])

print(marxes[::-1])

print(marxes.append('Zeppo')+'\n')

#############################

marxes = ['Groucho','Chico','Harpo','Zeppo']

others = ['Gummo','Karl']

marxes.extend(others)

print('marxes',marxes)




