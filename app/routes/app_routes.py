from flask import Flask, jsonify, request, redirect, url_for
from flask import current_app as app
import time

@app.route("/", methods=['GET', 'POST'])
def root():
    data = {}
    data['method'] = request.method
    data['data'] = 'Hello World!'
    app.logger.info(f"Response: ${data}")
    return jsonify(data)

from app.tasks import add

@app.route('/task', methods=['GET'])
def longtask():
    task = add.delay(5,5)
    return redirect(url_for('taskstatus', task_id=task.id))
    
@app.route('/status/<task_id>')
def taskstatus(task_id):
    task = add.AsyncResult(task_id)
    if not task.ready():
        response = {
            'queue_state': task.state,
            'status': 'Process is ongoing...',
            'status_update': url_for('taskstatus', task_id=task.id)
        }
    else:
        response = {
            'queue_state': task.state,
            'result': task.wait()
        }
    return jsonify(response)