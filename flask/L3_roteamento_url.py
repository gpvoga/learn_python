from flask import Flask, request, render_template

app = Flask("teste_url")

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


@app.route("/roteamento_variavel/<int:variavel>")
def teste_view1(variavel):
    return 'valor inteiro {}'.format(variavel), 200

@app.route("/roteamento_variavel/<float:variavel>")
def teste_view2(variavel):
    return 'valor float {}'.format(variavel), 200



app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=True)
