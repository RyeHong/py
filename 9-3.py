from flask import Flask,render_template
# Add a home() function to handle requests for the home page. Set it up to return the
# string It's alive!.

app = Flask(__name__,static_folder='.',static_path='')



@app.route('/')
def home():

    return app.send_static_file('index2.html')

app.run(port=5000,debug=True)


