from flask import Flask, request, jsonify
from connect import collection, collection2, collection3
app = Flask(__name__)

@app.route('/faturamento', methods=['GET'])
def faturamento():
    faturamento = collection.find({}, {'Valor Final': 1, '_id': 0})
    faturamento_list = list(faturamento)

    if faturamento_list:
        for item in faturamento_list:
            print(item)
        return jsonify(faturamento_list)
    else:
        print("Nenhum documento encontrado.")
        return jsonify({"message": "Nenhum documento encontrado."})


if __name__ == '__main__':
    app.run(debug=True)


