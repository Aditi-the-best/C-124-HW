from flask import Flask, app, jsonify, request
from data import data

app = Flask(__name__)
list=[
    {
        'id':1,
        'name':"Aditi",
        'contact':981222222
    }
]
@app.route("/")
def index():
    return jsonify({
        "data":list,
        "message":"successs!!" 
    })
@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "provide data!!!!!!!!"

        })

    contact ={
    'id':tasks[-1]["id"]+1,
    'Name' : request.json['Name'],  
    'Contact' : request.json.get('Contact',""),
    'done' : False

    }
    list.append(contact)
    return jsonify({
        "status":"success",
        "message":"contact added successfully"
    })
if __name__ == "__main__":
    app.run()
