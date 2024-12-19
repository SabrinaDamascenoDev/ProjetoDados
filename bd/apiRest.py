from flask import Flask, request, jsonify
from connect import collection, collection2, collection3
app = Flask(__name__)

@app.route('/faturamento', methods=['GET'])
def faturamento():
    faturamento = collection.find({}, {'Valor Final': 1, '_id': 0})
    faturamento_list = list(faturamento)

    if faturamento_list:
        return jsonify(faturamento_list), 200
    else:
        print("Nenhum documento encontrado.")
        return jsonify({"message": "Nenhum documento encontrado."}), 404

@app.route('/lojas', methods=['GET'])
def lojas():
    lojas = collection.find({}, {'ID Loja': 1, '_id': 0})
    lojas_list = list(lojas)
    if lojas_list:
        return jsonify(lojas_list), 200
    else:
        print("Nenhum documento encontrado.")
        return jsonify({"message": "Nenhum documento encontrado."}), 404

@app.route('/quantidade', methods=['GET'])
def quantidade():
    quantidade = collection2.find({}, {'Quantidade': 1, '_id':0})
    quantidade_list = list(quantidade)
    if quantidade_list:
        return jsonify(quantidade_list), 200
    else:
        print("Nenhum documento encontrado.")
        return jsonify({"message": "Nenhum documento encontrado."}), 404

@app.route('/ticket', methods=['GET'])
def ticket():
    ticket = collection3.find({}, {'Ticket Médio': 1, '_id': 0})
    quantidade_list = list(ticket)
    if quantidade_list:
        return jsonify(quantidade_list), 200
    else:
        print("Nenhum documento encontrado.")
        return jsonify({"message": "Nenhum documento encontrado."}), 404


if __name__ == '__main__':
    app.run(debug=True)


