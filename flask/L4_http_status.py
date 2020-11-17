from flask import Flask, abort

app = Flask("teste_status")


@app.route("/teste/<int:variavel>")
def url_shortener(variavel):
    try:
        lista = {1: 'teste1',
                 2: 'teste2'}
        url = lista[variavel]
        return url
    except AttributeError:
        # objeto NoneType não tem o atributo url, ou seja, # TODO não existe TUDO
        abort(404)
    except ConnectionError:
        # não conseguiu conectar no MySQL # TODO: Use o PostGres :)
        abort(503)  # ServiceUnavailable
    else:
        redirect('httpp://localhost:8080/teste')



@app.route("/teste")
def url_shortener2():
    return 'valor nao reconheciido', 200



app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=True)
