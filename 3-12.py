dictionary = [['dog','chien'],['cat','chat'],['walrus','morse']]
e2f = dict(dictionary)
f2e = dict((v,k) for k,v in e2f.items())



print('dictionary f2e is ',f2e)

