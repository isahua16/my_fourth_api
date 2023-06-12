from dbhelpers import run_statement
from apihelpers import check_data
from flask import Flask, request, make_response, jsonify
import uuid
app = Flask(__name__)

@app.post('/api/client')
def new_client():
    error = check_data(request.json, ['username', 'password'])
    if (error != None):
        return make_response(jsonify(error), 400)
    results = run_statement('call new_client(?,?)', [request.json.get('username'), request.json.get('password')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify('Something went wrong'), 500)

@app.post('/api/login')
def login_client():
    error = check_data(request.json, ['username', 'password'])
    if (error != None):
        return make_response(jsonify(error), 400)
    token = uuid.uuid4().hex
    results = run_statement('call login_client(?,?,?)', [request.json.get('username'), request.json.get('password'), token])
    if(type(results) == list and results != []):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify('Something went wrong'), 500)

@app.post('/api/post')
def create_post():
    error = check_data(request.json, ['token', 'content'])
    if (error != None):
        return make_response(jsonify(error), 400)
    results = run_statement('call create_post(?,?)', [request.json.get('token'), request.json.get('content')])
    if(type(results) == list and results != []):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify('Something went wrong'), 500)

app.run(debug=True)
