from flask import Flask, jsonify, request
from flask_cors import CORS

salario = 0
horasTrab = 0

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/salario', methods=['GET'])
def get_result():
    response_object = {'status': 'success'}
    response_object = {
        'horasTrab': horasTrab,
        'salario': salario,
    }
    return jsonify(response_object)

@app.route('/salario', methods=['POST'])
def post_numbers():
    post_data = request.get_json()
    salario = post_data.get("salario")
    horasTrab = post_data.get("horasTrab")
    print(salario)
    print(horasTrab)
    bruto = salario * horasTrab
    inss = bruto * 0.08
    impostoDeRenda = bruto * 0.11
    sindicato = bruto * 0.05
    salarioLiquido = bruto - inss - impostoDeRenda - sindicato

    response_object = {
        'salario': salario,
        'horasTrab': horasTrab,
        'bruto': bruto,
        'inss': inss,
        'renda': impostoDeRenda,
        'sindicato': sindicato,
        'salarioLiquido': salarioLiquido,
    }

    return jsonify(response_object)



if __name__ == '__main__':
    app.run()