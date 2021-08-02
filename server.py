# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 18:55:15 2021

@author: chauh
"""
#recive from  webhook
#use /webhook in tradingview webhook
from flask import Flask, request, abort



app = Flask(__name__)


# Create root to easily let us know its on/working.
@app.route('/')
def root():
    return 'online test'   

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    print('Hello Vikas')
    
    if request.method == 'POST':
         json_response = {}
         data = request.get_data(as_text=True)
         print(data)
         #return {'data': data}
         json_response['data'] = data
         return json_response
      
        
         #return 'success ping', 200  
    else:
        abort(400)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)
    print('Hello again')
    
    
    
    


    