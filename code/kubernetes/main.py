from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def chat():
    return jsonify({"response": "Hi I am an API"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
