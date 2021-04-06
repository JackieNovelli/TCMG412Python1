from flask import Flask, jsonify, Response, request
import os 
import socket 
import hashlib
import math
import requests
import redis
 
app = Flask(__name__) 


@app.route('/md5/<string>') 
def md5(string):
    hash_obj = hashlib.md5(string.encode('utf-8')) 
#   Response = jsonify("MD5_String"=hash_obj.hexdigest())
#   return Response
    return jsonify(
        input=string,
        output=hash_obj.hexdigest()
    )
 
@app.route('/factorial/<integer>') 
def factorial(integer):	
#   return jsonify("Factorial_Num"=math.factorial(int(integer)))
    try:
        return jsonify(
            input=integer,
            output=math.factorial(int(integer))
        )
    except:
        return Response(status=400)


@app.route('/fibonacci/<integer>')
def fibonacci(integer):
    try:
        n = int(integer)
        if int(integer) < 0:
            return Response(status=400)
        if int(integer) == 0:
            Fib_list = [0]
        else:
            Fib_list = [0,1,1]
            num = Fib_list[-1]
            while num < n:
                num = Fib_list[-2]+Fib_list[-1]
                if num <= n:
                    Fib_list.append(num)
    #   return jsonify("Fib_List"=Fib_list)
        return jsonify(
            input=integer,
            output=Fib_list
        )
    except:
        return Response(status=400)

@app.route('/is-prime/<integer>')
def is_prime(integer):
    try:
        integer = int(integer)
        if integer==1:
    #       return jsonify("Boolean_Value"="False")
            return jsonify(
                input=integer,
                output=False
            )
        elif (integer==2):
    #       return jsonify("Boolean_Value"="True")
            return jsonify(
                input=integer,
                output=True
            )
        else:
            for x in range(2,integer):
                if (integer % x==0):
    #               return jsonify("Boolean_Value"="False")
                    return jsonify(
                        input=integer,
                        output=False
                    )
    #   return jsonify("Boolean_Value"="True")
        return jsonify(
            input=integer,
            output=True
        )
    except:
        return Response(status=400)

@app.route('/slack-alert/<string>')
def slack_alert(string):
    string = str(string)
    url = 'https://hooks.slack.com/services/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'
    result = str(requests.post(url, json={'text':string, 'channel':"group-7"}))
    if result.find('200') != -1:
#       return jsonify("Boolean_Value"="True")
        return jsonify(
            input=string,
            output=True
        )
    else:
#       return jsonify("Boolean_Value"="False")
        return jsonify(
            input=string,
            output=False
        )

@app.route('/keyval', methods=['POST', 'PUT'])
def POST_PUT():
    redserv = redis.Redis(host="redis-server", port=6379)
    if request.method == 'POST':
        redserv.set(request.form['key'], request.form['value'])
    if request.method == 'PUT':
        redserv.set(request.form['key'], request.form['value'])

@app.route('/keyval/<string>', methods=['GET', 'DELETE'])
def GET_DELETE(string):
    red = redis.Redis(host="redis-server", port=6379, db=0)
    if request.method == 'GET':
        keyval = red.get(string)
        if keyval == None:
            return jsonify(
                key=string,
                value=str(keyval),
                command= str(f'GET {string}'),
                result= False,
                error='key not found'
            ), 404
        else:
            return jsonify(
                key=string,
                value=str(keyval),
                command= str(f'GET {string}'),
                result= True,
                error=''
            )

    if request.method == 'DELETE':
        red.delete(string)
        return

		
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)