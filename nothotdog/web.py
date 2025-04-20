from flask import Flask, render_template, request, jsonify
import requests
import json
import os
from dotenv import load_dotenv

#Load, initialize, and use Flask variables -- creating variables for url and a variable to prove to Hugging Face that we have an access token to interact with data on their end
load_dotenv()
API_URL = os.getenv("HUGGING_FACE_API_URL")
headers = {'Authorization': f'Bearer {os.getenv("HUGGING_FACE_API_KEY")}'}

app = Flask(__name__)

#queries hugging face model for when I recieve incoming image data from our form
def query(data):
    response = requests.request('POST', API_URL, headers=headers, data=data)
    return json.loads(response.content.decode('utf-8'))

#Adding the necessary routes in flask to host our web form and handle image data
#Routing to index.html template
@app.route('/')
def index():
    return render_template('./index.html')

#handling image uploads, sending to hugging face, and retrieving results of model predictions via helper function query() return value
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file1']
    modeldata = query(file)
    return jsonify(modeldata)

#internet location where we will run this program (Flask Dev environment host)
app.run(host='0.0.0.0', port=81)

