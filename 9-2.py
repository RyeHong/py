from flask import Flask
# Build a skeleton website, using Flask’s debug/reload development web server. Ensure
# that the server starts up for hostname localhost on default port 5000. If your computer
# is already using port 5000 for something else, use another port number.

app = Flask(__name__)
app.run(port= 5000,debug = True)

