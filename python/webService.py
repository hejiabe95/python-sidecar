import json
import time
from threadSecurityAlgorithm import run
from scheduler import scheduler
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
    scheduler.add_job(run, args=['job_once', ], id='job_once',replace_existing=True)
    result = 'success!'
    return Response(json.dumps(result), mimetype='application/json')

scheduler.start()
app.run(host='0.0.0.0', port=3000, threaded=True)

