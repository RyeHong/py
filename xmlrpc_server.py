from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime
def double():
    return datetime.now().isoformat()
server = SimpleXMLRPCServer(("localhost", 6789))
server.register_function(double, "double")
server.serve_forever()