from flask import Flask, render_template, request
from azure.cosmos import exceptions, CosmosClient, PartitionKey

endpoint = "https://flaskcosmosdb.documents.azure.com:443/"
key = 'u7A8wUOPapm3uyHG8PkduwQPsc4zlvmTxG9CfWvzocQHfhaNaaPtURSMzH6Y0Mdih52FnCP56xPw9fWvb3aOtA=='
client = CosmosClient(endpoint, key)
database_name = 'flaskdb'
database = client.get_database_client(database_name)
container_name = 'flaskcontainer'
container = database.get_container_client(container_name)





app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def form_details():
    # text = {'Sensor': request.form["SensorId"], 'Plantname': request.form["Plantname"],
    #        'Country': request.form["Country"]}
    # print(text)
    container.upsert_item({
        'category': 'Plant Details',
        'Sensor': request.form["SensorId"],
        'Plantname': request.form["Plantname"],
        'Country': request.form["Country"]
    }
    )
    return "Done"

    #return jsonify(text)


app.run(host='localhost', port=5000)