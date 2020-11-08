from flask import Flask, request, render_template

app = Flask("flask_voga")


@app.route("/<name>")
def index(name):
    if name.lower() == "voga":
        return "Olá {}".format(name), 200
    else:
        return "Not Found", 404

app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=True)