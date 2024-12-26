from flask import Flask
import serverless_wsgi

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

def lambda_handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

