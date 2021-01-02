from flask import Flask 
app = Flask(__name__)

@app.route('/')
def jobs():
    render_template('index.html')