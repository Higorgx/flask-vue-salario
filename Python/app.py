from flask import Flask, jsonify, request
from flask_cors import CORS

salarioHora = 0
horasTrab = 0

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/salario', methods=['GET'])
def get_result():
    response_object2 = {'status': 'success'}
    response_object2['Hora trabalhadas'] = horasTrab
    response_object = {'status': 'success'}
    response_object['salario Hora'] = horasTrab
    return jsonify(response_object, response_object2)

@app.route('/salario', methods=['POST'])
def post_numbers():
    post_data = request.get_json()
    salarioHora = post_data.get("salarioHora")
    horasTrab = post_data.get("horasTrab")

    print(salarioHora)
    print(horasTrab)

    salarioBruto = salarioHora * horasTrab
    inss = salarioBruto * 0.08
    impostoDeRenda = salarioBruto * 0.11
    sindicato = salarioBruto * 0.05
    salarioLiquido = salarioBruto - inss - impostoDeRenda - sindicato

    response_object = {
        'Bruto': salarioBruto,
        'inss': inss,
        'renda': impostoDeRenda,
        'sindicato': sindicato,
        'salarioLiquido': salarioLiquido
    }

    return jsonify(response_object)



if __name__ == '__main__':
    app.run()