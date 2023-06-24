from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def myapp():
    message = f"To use this app: {request.base_url[:-1]}:5000/data?date=YYYYMMDD"
    return message

