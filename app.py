from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def page():
    return "This is a the World Food Programme food hotspot tracking project."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9393)