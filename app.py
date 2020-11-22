# app.py

# Required imports
import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('todos')


@app.route('/update/', methods=['GET']) #'POST', 'PUT'
def update():
    """
        update() : Update document in Firestore collection with request body.
        Ensure you pass a custom IsD as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    name = "" #projects/munchies-a2feb/databases/(default)/documents/foodEaten/zskIV2hw6vmxnH3RPJXg
    fields = ""
    rfidTag = "D4078AC3"
    amount = request.args.get('arg1')

    doc_ref = db.collection(u'foodEaten').document(u'zskIV2hw6vmxnH3RPJXg')
    doc_ref.set({
        #u'name': name,
        u'rfidTag': rfidTag,
        u'amount': amount    

    })

    return "Hello world"

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)