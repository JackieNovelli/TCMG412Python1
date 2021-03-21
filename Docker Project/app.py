from flask import Flask, jsonify
import os 
import socket 
import hashlib 
import math
import requests
 
app = Flask(__name__) 
 
@app.route('/md5/<string>') 
def md5(string):
    hash_obj = hashlib.md5(string.encode('utf-8')) 
    response = jsonify({"MD5_String": hash_obj.hexdigest()})
    return response
 
@app.route('/factorial/<integer>') 
def factorial(integer):	
    return jsonify({"Factorial_Num": math.factorial(int(integer))})

@app.route('/fibonacci/<integer>')
def fibonacci(integer):
    n = int(integer)
    Fib_list = [0,1]
    num = Fib_list[-1]
    while num < n:
        num = Fib_list[-2]+Fib_list[-1]
        if num < n:
            Fib_list.append(num)
    return jsonify({"Fib_List": Fib_list})

@app.route('/is-prime/<integer>')
def is_prime(integer):
    integer = int(integer)
    if integer==1:
        return jsonify({"Boolean_Value": "False"})
    elif (integer==2):
        return jsonify({"Boolean_Value": "True"})
    else:
        for x in range(2,integer):
            if (integer % x==0):
                return jsonify({"Boolean_Value": "False"})
    return jsonify({"Boolean_Value": "True"})

@app.route('/slack-alert/<string>')
def slack_alert(string):
    string = str(string)
    url = 'https://hooks.slack.com/services/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'
    result = str(requests.post(url, json={'text': string, 'channel': "group-7"}))
    if result.find('200') != -1:
        return jsonify({"Boolean_Value": "True"})
    else:
        return jsonify({"Boolean_Value": "False"})
		
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)