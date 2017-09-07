from flask import Flask,render_template,request
# Modify your server’s home() function to use the home.html template. Provide it with
# three GET parameters: thing, height, and color

app = Flask(__name__,static_folder='.',static_path='')


#
# @app.route('/')
# def home():
#
#     return app.send_static_file('home.html')


def home():

        return render_template('home.html',thing='dj',height='dkjl',color = 'djl')
# @app.route('/echo/')
# def echo():
#     thing = request.args.get('thing')
#     height = request.args.get('height')
#     color = request.args.get('color')
#     return render_template('home.html', thing=thing, height = height,color = color)

app.run(port=9999,debug=True)
