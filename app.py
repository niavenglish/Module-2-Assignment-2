from flask import Flask, jsonify, request


app = Flask(__name__)



@app.route("/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "World")
    return jsonify({"message": f"Hello, {name}!"}), 200

@app.route("/sum", methods=["POST"])
@app.route("/sum", methods=["POST"])
def sum_numbers():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object"}), 400

    if "numbers" not in data:
        return jsonify({"error": "Missing required field: 'numbers'"}), 400

    numbers = data["numbers"]

    if not isinstance(numbers, list):
        return jsonify({"error": "'numbers' must be a list"}), 400

    for n in numbers:
        if not isinstance(n, (int, float)):
            return jsonify({"error": "All items in 'numbers' must be numeric"}), 400

    return jsonify({"sum": sum(numbers)}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
