from flask import Flask, request, make_response, redirect, escape

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    user_ip = escape(user_ip)
    return f'Hello World Juan, tu IP es {user_ip}'