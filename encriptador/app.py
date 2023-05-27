from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/hash', methods=['POST'])
def hash_string():
    data = request.get_json()
    string_to_hash = data['string_to_hash']
    result = hashlib.sha256(string_to_hash.encode()).hexdigest()
    return jsonify({'hash': result})

if __name__ == "__main__":
    app.run(debug=True)