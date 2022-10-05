from flask import Flask, jsonify, request, json

app = Flask(__name__)

db_users = []

 # http://127.0.0.1:5000/user
@app.route("/user", methods = ['POST', 'GET'])
def create():
    if request.method == 'POST':
        date = request.json
        print (request.json['name'])
        if(date == False and []):
            return "Данные не введены", 403
        if (date ["name"] ==''):
            return "Имя не введено", 403

        db_users.append(date["name"])
        db_users.append(date["email"])
        db_users.append(date["password"])
        db_users.append(date["number"])
        return "Данные сохранены", 200

    if request.method == 'GET':
        return db_users, 200
    
    return jsonify (date)

@app.route('/user/<id>', methods=["DELETE"])

 # http://127.0.0.1:5000/user
@app.route("/music", methods = ['POST', 'GET'])
def create():
    if request.method == 'POST':
        date = request.json
        if(date== False and []):
            return "Данные не введены", 403
        if (date ["name"] ==''):
            return "Исполнитель не введен", 403

        db_users.append(date["name"])
        db_users.append(date["duration"])
        db_users.append(date["genre"])

        return "Данные сохранены", 200

    if request.method == 'GET':
        return db_users, 200
    
    return jsonify (date)