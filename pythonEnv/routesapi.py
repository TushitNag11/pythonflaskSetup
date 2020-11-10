from flask import Flask, render_template, request, redirect, url_for, jsonify

import json
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

""" 
1.	/team [method=Get]
	Returns the student names (your team members)
"""

@app.route("/team")
def devTeam():
    m1 = "<h4>Agam Choudhary</h4>"
    m2 = "<h4>Agam Choudhary</h4>"
    m3 = "<h4>Agam Choudhary</h4>"
    m4 = "<h4>Agam Choudhary</h4>"
    return "<h1>Meet Group 2</h1>\n{}\n{}\n{}\n{}".format(m1, m2, m3, m4)

""" 
2.	/data  [method=Get]
a.	Use https://mockaroo.com/ to create a json file
i.	Filename: customer.json
ii.	Fields:
{
  "first_name": "Daniella",
  "last_name": "Cheke",
  "pet": "Rattlesnake, dusky",
  "possible": [
    {
      "name": "Hamlin"
    }
  ]
}
b.	Returns the contents of the file and display to a browser

"""

@app.route("/data")
def getCustomers():
    if os.path.exists("./static/customer.json"):
        with open("./static/customer.json") as inputFile:
            data = json.load(inputFile)
        return render_template("jsonTable.html", n=len(data), customers=data)

""" 
3.	/add	[method=POST]
a.	the “client” sends a json formatted data to the server 
i.	the data contains first_name and last_name
b.	the data should be saved to a file on the server (filename: dummyData.json)
i.	update/append the new data (don’t override the previously saved data)

"""

@app.route('/add', methods=['POST'])
def dummyDataProcessing():
    data = request.get_json()
    fs = data[0]["first_name"] | None
    print("data:")
    print(fs)
    if fs is None:
        return jsonify({"message":"text not found"})
    else:
        with open('./datatemp/dummy.json','a+') as dummyfile:
            json.dump(data, dummyfile)
        return jsonify({"message":"Data Saved"})