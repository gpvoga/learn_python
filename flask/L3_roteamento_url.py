from flask import Flask, request, render_template

app = Flask("wtf")

@app.route("/roteamento_url")
@app.route("/roteamento_url/<pais>")
@app.route("/roteamento_url/<pais>/<estado>")
def lista_de_noticias(pais=None, estado=None):
    cat = request.args.get("categoria")
    qty = request.args.get("quantidade")

    return render_template("L3_roteamento_url.html",
                           pais=pais, estado=estado,
                           categoria=cat,
                           quantidade=qty), 200

app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=True)