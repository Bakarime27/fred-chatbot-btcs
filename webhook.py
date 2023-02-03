from flask import Flask, request, jsonify

#Initialise the app
app = Flask(__name__)

#Create a route for webhook
@app.route('/webhook', methods=['GET','POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    query_result = req.get('queryResult')
    if ("basse" in query_result['queryText'] or query_result['parameters']['type-maison'] == "basse") and query_result['parameters']['nombre-piece'] == 3:
        return jsonify({"fulfillmentText": 'Voilà un modèle qui pourrait vous intéresser :\n https://ohelinternational.net/produit/villa-basse-03-pieces/' })

    elif ("basse" in query_result['queryText'] or query_result['parameters']['type-maison'] == "basse") and query_result['parameters']['nombre-piece'] == 4:
        return jsonify({"fulfillmentText": 'Voilà un modèle qui pourrait vous intéresser :\n https://ohelinternational.net/produit/villa-basse-04-pieces/' })

    elif ("duplex" in query_result['queryText'] or query_result['parameters']['type-maison'] == "duplex") and query_result['parameters']['nombre-piece'] == 5:
        return jsonify({"fulfillmentText": 'Voilà un modèle qui pourrait vous intéresser :\n https://ohelinternational.net/produit/villa-duplex-05-pieces/' })
    else:
        return jsonify({"fulfillmentText": 'Nous n\'avons pas pour l\'instant de bien correspondant à votre demande' })
# run Flask app
if __name__ == "__main__":
    app.run()
