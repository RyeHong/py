import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
# num = 7

result = proxy.double()

print("Double %s " % ( result))
