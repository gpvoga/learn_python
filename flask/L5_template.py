from flask import Flask, render_template


app = Flask("teste_status")


@app.route("/html_page/<nome>")
def html_page(nome):
    return render_template("L5_template.html", nome=nome, nome2='voga')





app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=True)
