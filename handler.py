#This is a Flask web application that defines two routes, /health and /getReport/<input_string>.
#The /health route simply returns a "Pong" response to indicate that the server is up and running.

#The /getReport/<input_string> route accepts a POST request with an input string as a parameter. 
#It then instantiates a GenerateReport object and calls its generateReport method with the input 
#string. The response is returned as a JSON object.

from flask import Flask, request, Response, jsonify
from flask_cors import CORS
from generateReport import GenerateReport
import os

app = Flask(__name__)
CORS(app)

#see if api is working
@app.route('/health')
def health():
    return Response('Pong', status=200, mimetype='application/json')

#make prediction
@app.route('/getReport/<input_string>', methods=["POST"])
def getReport(input_string):
    generate_report = GenerateReport()
    response = generate_report.generateReport(input_string)
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)