from flask import Flask
from flask import jsonify
from flask import request
import json
import re


app = Flask(__name__)

#Open the NoSQL database
with open('data.json') as f:
    allmessages = json.load(f)


#List all messages
@app.route('/', methods=['GET'])
def ListAll():
    return jsonify({'all messages' : allmessages})

#Retrieve a specific message
@app.route('/qlink/<string:msg>', methods=['GET'])
def retriveMessage(msg):
    if messageExist(msg):
        return jsonify({'Retrived Message' : msg + " is " + allmessages.get(msg)})
    else:
        return jsonify({'Error': "Message doesnt exist" })



#Create a new message
@app.route('/qlink', methods=['POST'])
def createMessage():
    msg = jsonTostring()
    return detailsUpdate(msg)


#Update a message
@app.route('/qlink/<string:msg>', methods=['PUT'])
def UpdateMessage(msg):
    if messageExist(msg):
        allmessages.pop(msg, None)
        msg = jsonTostring()
        return detailsUpdate(msg)
    else:
        return jsonify({'Error': "Message doesnt exist"})


#Delete a message
@app.route('/qlink/<string:msg>', methods=['DELETE'])
def deleteMessage(msg):
    if messageExist(msg):
        allmessages.pop(msg, None)
        updateData()
        return jsonify({msg : "now deleted"})
    else:
        return jsonify({'Error': "Message doesnt exist"})


#check if message exist
def messageExist(msg):
    if msg in allmessages:
        return True
    False


#This method calls the palidrome method to check if a message is palidrome or not.
#It then updates the details of the message
def detailsUpdate(msg):

    if paliStatus(msg) is True:
        allmessages[msg] = "a Palidrome"
    else:
        allmessages[msg] = "not a Palidrome"

    updateData()
    details = allmessages[msg]
    return jsonify({'Message': msg + ' -> Is ' + details})


#Convert json input to String
def jsonTostring():
    msg = request.get_json()
    return list(msg.keys())[0]


#Adds or update modified record in the database
def updateData():
    with open('data.json', "w") as f:
        json.dump(allmessages, f)


# function which return reverse of a string
def paliStatus(s):

    #remove all non-alphabet from string
    regex = re.compile('[^a-zA-Z]')

    # First parameter is the replacement, second parameter is your input string
    s = regex.sub('', s).lower()

    #reverse the string
    reverseS = s[::-1]


    #Checking if both string and reverse string are equal or not
    if (s == reverseS):
        return True
    return False

if __name__ == "__main__":
    app.run(debug=True)