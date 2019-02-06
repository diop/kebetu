from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Only a fool tests the depth of a river with both feet'
