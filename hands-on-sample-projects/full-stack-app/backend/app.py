from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Backend is working!"

@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "Hello from the backend!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)