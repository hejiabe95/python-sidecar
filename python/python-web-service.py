import algorithm
import json
import time
from flask import Flask, Response, request
app = Flask(__name__)
@app.route("/health")
def health():
    result = {'status': 'UP'}
    return Response(json.dumps(result), mimetype='application/json')
@app.route("/hello")
def hello():
    result = {'username': 'admin', 'password': 'admin'}
    time.sleep(1)
    return Response(json.dumps(result), mimetype='application/json')
@app.route("/execute", methods= ['get','post'] )
def excute():
    result = {'times': request.args.get('times'), 'algorithm': algorithm.algorithm_start()}
    return Response(json.dumps(result), mimetype='application/json')
app.run(host='0.0.0.0', port=3000, threaded=True)