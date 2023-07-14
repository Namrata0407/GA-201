from flask import Flask,jsonify,request
import json
app = Flask(__name__)

users = [
    {"id":1, "name":"abcd", "comment":"ok"},
     {"id":2, "name":"efgh", "comment":"notok"},
      {"id":3, "name":"ijkl", "comment":"ok"}
]

# for Post Creation

@app.route("/post", methods = ["POST"])
def create():
    enter_data = request.json
    users.append(enter_data)

    responce = jsonify({"message":"post added successfully"})
    responce.status_code = 200
    return responce

# for Post Viewing

@app.route("/",methods={"GET"})
def read():
    responce = jsonify({"message":users})
    responce.status_code = 200
    return responce


# for Post Deletion

@app.route("/post", methods = ["DELETE"])
def delete(index):
    global users
    newOBj = []

    for i in users:
        if i["id"] == int(index):
            continue
        else:
            newOBj.append(i)
            users = newOBj
    responce = jsonify({"message":users})
    responce.status_code = 200
    return responce


if __name__ == "_main_":
   app.run(debug=True)