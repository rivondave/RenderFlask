from flask import Flask , jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def app_def():
    return jsonify({"message":"This is a flask API"})

if __name__ == "__main__":
    app.run(debug=True)