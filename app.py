from flask import Flask, jsonify, request

# Create the Flask application
app = Flask(__name__)


# GET /hello?name=Alice  ->  {"message": "Hello, Alice!"}
@app.route("/hello", methods=["GET"])
def hello():
    # Read the optional "name" from the URL; use "World" if it's missing
    name = request.args.get("name", "World")
    return jsonify({"message": f"Hello, {name}!"}), 200

# POST /sum  with body {"numbers": [1, 2, 3]}  ->  {"sum": 6}
@app.route("/sum", methods=["POST"])
@app.route("/sum", methods=["POST"])
def sum_numbers():
    # silent=True returns None instead of crashing if the JSON is invalid
    data = request.get_json(silent=True)

    # Check 1: the body must be a JSON object (dictionary)
    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object"}), 400

    # Check 2: the "numbers" field must exist
    if "numbers" not in data:
        return jsonify({"error": "Missing required field: 'numbers'"}), 400

    numbers = data["numbers"]

    # Check 3: "numbers" must be a list
    if not isinstance(numbers, list):
        return jsonify({"error": "'numbers' must be a list"}), 400

    # Check 4: every item in the list must be a number
    for n in numbers:
        if not isinstance(n, (int, float)):
            return jsonify({"error": "All items in 'numbers' must be numeric"}), 400

    # If we get here, the input is valid
    return jsonify({"sum": sum(numbers)}), 200


# Run the server on port 5000 when you type: python app.py
if __name__ == "__main__":
    app.run(port=5000, debug=True)
