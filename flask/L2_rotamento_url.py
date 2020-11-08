from flask import Flask, request, render_template

app = Flask("wtf")

@app.route("/roteamento_url/<pais>")
def lista_de_noticias(pais):
    cat = request.args.get("categoria")
    qty = request.args.get("quantidade")

    return render_template("L2_roteamento_url.html", pais=pais, categoria=cat, quantidade=qty), 200

app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=True)