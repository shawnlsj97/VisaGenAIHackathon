from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify(message='Hello, World!')

@app.route('/chat', methods=['POST'])
def chat():
    body = request.get_json()
    return jsonify(message='message received', status=200)

if __name__ == '__main__':
    app.run(debug=True)