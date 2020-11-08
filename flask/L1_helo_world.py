from flask import Flask

app = Flask(__name__)

@app.route("/helloworld")
def hello_world():
    return "Hello World! <strong>I am learning Flask</strong>", 200


app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=True)
