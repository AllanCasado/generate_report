from flask import Flask, request, Response, jsonify
from generateReport import GenerateReport
import os

app = Flask(__name__)

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