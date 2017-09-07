dictionary = [['dog','chien'],['cat','chat'],['walrus','morse']]
e2f = dict(dictionary)
f2e = dict((v,k) for k,v in e2f.items())

print("f2e chien =",f2e['chien'])



