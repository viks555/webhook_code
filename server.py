# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 18:55:15 2021

@author: chauh
"""
#recive from  webhook
#use /webhook in tradingview webhook
from flask import Flask, request, abort
import json


app = Flask(__name__)


# Create root to easily let us know its on/working.
@app.route('/')
def root():
    return 'online test'   

@app.route('/webhook', methods=['POST','GET'])
def webhookrec():
    print('Hello Vikas')
    
    if request.method == 'POST':
         #request.encoding = 'ISO-8859-1'
         json_response = {}
         #json_response= request.get_data(as_text=True)
         json_response=request.get_json(force=True)
         #json_response= request.get_json()
         #json_response = json.load(request)
         #data = json.loads(request.data)
        # print(data)
         #print(json_response)
         print(json_response['orders'])
         #print(type(json_response))
         #print(json.loads(json_response))
         #print(data['scrip'])
         #return {'data': data}
         #print(json_response["scrip"])
         
         return json_response['orders'] 
    
       
         #return 'success ping', 200  
    else:
        abort(400)

#out1=webhookrec()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)
    print('Hello again')
    
      
    
    


with app.test_request_context(
        'C:/Users/chauh/make_report/2017', data={'format': 'short'}):
    webhookrec()
    
    