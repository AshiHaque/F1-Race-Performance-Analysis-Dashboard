from flask import Flask, jsonify, request
from flask_cors import CORS
from Circuits import get_circuit_info, get_all_circuit_names

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/circuits', methods=['GET'])
def get_circuit_info_route():
    circuit_name = request.args.get('circuit_name')
    if not circuit_name:
        return jsonify({"error": "Circuit name not provided"})

    circuit_info = get_circuit_info(circuit_name)
    return jsonify(circuit_info)

@app.route('/circuits/names', methods=['GET'])
def get_all_circuit_names_route():
    circuit_names = get_all_circuit_names()
    return jsonify(circuit_names)

if __name__ == '__main__':
    app.run(debug=True)
