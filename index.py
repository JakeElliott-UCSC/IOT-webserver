from flask import Flask, request, jsonify

app = Flask(__name__)

library = {}
wtr_weather = 0
esp_weather = 0

# GET
# HOME ===================================================================
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the simple web server!\n"

# POST
# DATA ===================================================================
@app.route('/data', methods=['POST'])
def receive_data():
    global library
    data = request.json
    for key in data:
        library.update({key:data.get(key)})
    return jsonify({"message": "Data received", "data": data}), 200

# GET
# DATA ===================================================================
@app.route('/data', methods=['GET'])
def report_data():
    return jsonify(library), 200

# GET
# INFO ===================================================================
@app.route('/info', methods=['GET'])
def get_info():
    info = {
        "name": "Simple Web Server",
        "version": "1.0",
        "description": "A simple web server that handles GET and POST requests."
    }
    return jsonify(info)

# POST
# WTHR ===================================================================
# Recieve weather from esp
@app.route('/weather', methods=['POST'])
def receive_weather():
    global wtr_weather
    global esp_weather

    data = request.json

    esp_weather = int(data.get("weather"))

    print("\n\n\n\n ESP WEATHER: " + esp_weather + "\n\n\n\n")
    
    return jsonify({"message": "Data received", "data": esp_weather}), 200

# GET
# WTHR ===================================================================
@app.route('/weather', methods=['GET'])
def report_weather():
    global wtr_weather
    global esp_weather
    return jsonify({"weather":esp_weather}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
