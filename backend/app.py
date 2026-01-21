from flask import Flask, jsonify, request, send_from_directory
import os

app = Flask(__name__, static_folder='../frontend')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/status')
def status():
    return jsonify({
        "status": "online",
        "services": ["calculator", "chatbot", "converter", "humanizer"]
    })

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Mock authentication
    if username == "admin" and password == "password123":
        return jsonify({"success": True, "message": "Login successful!", "token": "mock-jwt-token"})
    return jsonify({"success": False, "message": "Invalid credentials"}), 401

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    print("Server starting on http://localhost:5000")
    app.run(debug=True, port=5000)
