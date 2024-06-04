from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the simple web server!"

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    return jsonify({"message": "Data received", "data": data}), 200

@app.route('/info', methods=['GET'])
def get_info():
    info = {
        "name": "Simple Web Server",
        "version": "1.0",
        "description": "A simple web server that handles GET and POST requests."
    }
    return jsonify(info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
