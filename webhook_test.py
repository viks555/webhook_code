# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 09:49:54 2021

@author: i0853
"""

from flask import Flask, request, abort
import json

import logging
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

kite = KiteConnect(api_key="your_api_key")

# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
# Once you have the request_token, obtain the access_token
# as follows.

data = kite.generate_session("request_token_here", api_secret="your_secret")
kite.set_access_token(data["access_token"])




app = Flask(__name__)

client = Client(config.API_KEY, config.API_SECRET, tld='us')

def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print(f"sending order {order_type} - {side} {quantity} {symbol}")
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False

    return order


# Create root to easily let us know its on/working.
@app.route('/')
def root():
    return 'online test'   

@app.route('/webhook', methods=['POST','GET'])
def webhookrec():
    print('Hello Vikas')
    
    if request.method == 'POST':
         #request.encoding = 'ISO-8859-1'
         data = json.loads(request.data)
         
         print(data['orders'][1]['symbol'])
         sym=data['orders'][1]['symbol']
        
         return data['orders'][1]['symbol']
    
    
         #return 'success ping', 200  
    else:
        abort(400)

#out1=webhookrec()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)
    print('Hello again')
    
      