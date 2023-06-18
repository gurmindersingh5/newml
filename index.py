from flask import Flask, Response

app = Flask(__name__)

app.config['SECRET_KEY'] = "lovely17"

    

@app.route('/')
def home():
    return Response("welcome")
