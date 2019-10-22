import json
import time
from scheduler import scheduler
from algorithm import algorithm_start
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
    scheduler.add_job(algorithm_start, args=['job_once', ], id='job_once',replace_existing=True)
    result = 'success!'
    return Response(json.dumps(result), mimetype='application/json')

scheduler.start()
app.run(host='0.0.0.0', port=3000, threaded=True)

