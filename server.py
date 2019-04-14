from flask import Flask, request
from faker import Faker
from flask import jsonify
fake = Faker()
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    name = fake.name()
    email = fake.email()
    response = {
        "name": name,
        "email": email
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')