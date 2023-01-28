from .models import User, order1, adminorder,adminorder1,orderdetails1,order2, OrderDetails, WithdrawModel, BotCount,Transaction

import time

import random
import email
import jwt
import json
import pandas as pd
from binance import Client
from binance import BinanceSocketManager
import requests

def place():
    sam = adminorder1.objects.filter(type = "NLIMIT")
    if sam:
        for limit in sam:
            symbol = limit.symbol
            side = limit.side
            if limit.trade == "Future":
                key = "https://fapi.binance.com/fapi/v1/ticker/24hr?symbol="+symbol
                data1 = requests.get(key)
                data1 = data1.json()
                price1 = float(data1['lastPrice'])
                if limit.side == "BUY":
                    if price1 <= float(limit.price):
                        sam = User.objects.get(email = limit.Owner)
                        balance = float(sam.future) *float(limit.percentage)
                        qty = round(((balance*int(limit.leverage))/(price1/1000))/1000, 4)
                        buyusdt = qty * price1
                        sam.future = float(sam.future) - balance
                        sam.save()
                        comission = (buyusdt * 0.08)/100
                        post5 = orderdetails1(symbol=symbol,balance = balance,owner=sam.email, buyprice = price1, buyusdt=buyusdt, leverage=int(limit.leverage),orderid=limit.orderid,comission=comission,qty=qty,side=limit.side)
                        post5.save()
                        post = order2(Order_id =limit.orderid,trade="Future",Symbol=symbol,Owner = sam.email,side = limit.side,Price = price1,quantity = qty)
                        post.save()
                if limit.side == "SELL":
                    if price1 >= float(limit.price):
                        sam = User.objects.get(email = limit.Owner)
                        balance = float(sam.future) *float(limit.percentage)
                        qty = round(((balance*int(limit.leverage))/(price1/1000))/1000, 4)
                        sellusdt = qty * price1
                        sam.future = float(sam.future) - balance
                        sam.save()
                        comission = (buyusdt * 0.08)/100
                        post5 = orderdetails1(symbol=symbol,balance = balance,owner=sam.email, sellprice = price1, sellusdt=sellusdt, leverage=int(limit.leverage),orderid=limit.orderid,comission=comission,qty=qty,side=limit.side)
                        post5.save()
                        post = order2(Order_id =limit.orderid,trade="Future",Symbol=symbol,Owner = sam.email,side = limit.side,Price = price1,quantity = qty)
                        post.save()
            if limit.trade == "Spot":
                key = "https://api.binance.com/api/v3/ticker/price?symbol="+symbol
                data1 = requests.get(key)
                data1 = data1.json()
                price1 = float(data1['price'])
                if limit.side == "BUY":
                    if price1 <= float(limit.price):
                        sam = User.objects.get(email = limit.Owner)
                        balance = float(sam.spot) *float(limit.percentage)
                        qty = round(((balance)/(price1/1000))/1000, 4)
                        buyusdt = qty * price1
                        sam.spot = float(sam.spot) - balance
                        sam.save()
                        comission = (buyusdt * 0.08)/100
                        post5 = orderdetails1(symbol=symbol,balance = balance,owner=sam.email, buyprice = price1, buyusdt=buyusdt, leverage=int(limit.leverage),orderid=limit.orderid,comission=comission,qty=qty,side=limit.side)
                        post5.save()
                        post = order2(Order_id =limit.orderid,trade="Spot",Symbol=symbol,Owner = sam.email,side = limit.side,Price = price1,quantity = qty)
                        post.save()
                if limit.side == "SELL":
                    if price1 >= float(limit.price):
                        sam = User.objects.get(email = limit.Owner)
                        balance = float(sam.spot) *float(limit.percentage)
                        qty = round(((balance)/(price1/1000))/1000, 4)
                        sellusdt = qty * price1
                        sam.spot = float(sam.spot) - balance
                        sam.save()
                        comission = (buyusdt * 0.08)/100
                        post5 = orderdetails1(symbol=symbol,balance = balance,owner=sam.email, sellprice = price1, sellusdt=sellusdt, leverage=int(limit.leverage),orderid=limit.orderid,comission=comission,qty=qty,side=limit.side)
                        post5.save()
                        post = order2(Order_id =limit.orderid,trade="Spot",Symbol=symbol,Owner = sam.email,side = limit.side,Price = price1,quantity = qty)
                        post.save()


def place1():
    sam = adminorder1.objects.filter(type = "SLIMIT")
    if sam:
        for limit in sam:
            symbol = limit.symbol
            side = limit.side
            if limit.trade == "Future":
                key = "https://fapi.binance.com/fapi/v1/ticker/24hr?symbol="+symbol
                data1 = requests.get(key)
                data1 = data1.json()
                price1 = float(data1['lastPrice'])
                if limit.side == "BUY":
                    if price1 >= float(limit.price):
                        sam = User.objects.get(email = limit.Owner)
                        balance = float(sam.future) *float(limit.percentage)
                        qty = round(((balance*int(limit.leverage))/(price1/1000))/1000, 4)
                        buyusdt = qty * price1
                        sam.future = float(sam.future) - balance
                        sam.save()
                        comission = (buyusdt * 0.08)/100
                        post5 = orderdetails1(symbol=symbol,balance = balance,owner=sam.email, buyprice = price1, buyusdt=buyusdt, leverage=int(limit.leverage),orderid=limit.orderid,comission=comission,qty=qty,side=limit.side)
                        post5.save()
                        post = order2(Order_id =limit.orderid,trade="Future",Symbol=symbol,Owner = sam.email,side = limit.side,Price = price1,quantity = qty)
                        post.save()
                if limit.side == "SELL":
                    if price1 <= float(limit.price):
                        sam = User.objects.get(email = limit.Owner)
                        balance = float(sam.future) *float(limit.percentage)
                        qty = round(((balance*int(limit.leverage))/(price1/1000))/1000, 4)
                        sellusdt = qty * price1
                        sam.future = float(sam.future) - balance
                        sam.save()
                        comission = (buyusdt * 0.08)/100
                        post5 = orderdetails1(symbol=symbol,balance = balance,owner=sam.email, sellprice = price1, sellusdt=sellusdt, leverage=int(limit.leverage),orderid=limit.orderid,comission=comission,qty=qty,side=limit.side)
                        post5.save()
                        post = order2(Order_id =limit.orderid,trade="Future",Symbol=symbol,Owner = sam.email,side = limit.side,Price = price1,quantity = qty)
                        post.save()
            if limit.trade == "Spot":
                key = "https://api.binance.com/api/v3/ticker/price?symbol="+symbol
                data1 = requests.get(key)
                data1 = data1.json()
                price1 = float(data1['price'])
                if limit.side == "BUY":
                    if price1 >= float(limit.price):
                        sam = User.objects.get(email = limit.Owner)
                        balance = float(sam.spot) *float(limit.percentage)
                        qty = round(((balance)/(price1/1000))/1000, 4)
                        buyusdt = qty * price1
                        sam.spot = float(sam.spot) - balance
                        sam.save()
                        comission = (buyusdt * 0.08)/100
                        post5 = orderdetails1(symbol=symbol,balance = balance,owner=sam.email, buyprice = price1, buyusdt=buyusdt, leverage=int(limit.leverage),orderid=limit.orderid,comission=comission,qty=qty,side=limit.side)
                        post5.save()
                        post = order2(Order_id =limit.orderid,trade="Spot",Symbol=symbol,Owner = sam.email,side = limit.side,Price = price1,quantity = qty)
                        post.save()
                if limit.side == "SELL":
                    if price1 <= float(limit.price):
                        sam = User.objects.get(email = limit.Owner)
                        balance = float(sam.spot) *float(limit.percentage)
                        qty = round(((balance)/(price1/1000))/1000, 4)
                        sellusdt = qty * price1
                        sam.spot = float(sam.spot) - balance
                        sam.save()
                        comission = (buyusdt * 0.08)/100
                        post5 = orderdetails1(symbol=symbol,balance = balance,owner=sam.email, sellprice = price1, sellusdt=sellusdt, leverage=int(limit.leverage),orderid=limit.orderid,comission=comission,qty=qty,side=limit.side)
                        post5.save()
                        post = order2(Order_id =limit.orderid,trade="Spot",Symbol=symbol,Owner = sam.email,side = limit.side,Price = price1,quantity = qty)
                        post.save()

def place2():
    sam = adminorder1.objects.filter(type="SL")
    if sam:
        for limit in sam:
            de = adminorder1.objects.filter(orderid = limit.orderid)
            try:
                sa = de.get(type = "SLIMIT")
            except:
                sa = "NA"
            try:
                ma = de.get(type = "NLIMIT")
            except:
                ma = "NA"
            if sa=="NA" and ma == "NA":
                userdata = order2.objects.get(Order_id=limit.orderid)
                symbol = userdata.Symbol
                key = "https://api.binance.com/api/v3/ticker/price?symbol="+symbol
                data1 = requests.get(key)
                data1 = data1.json()
                side = userdata.side
                qty = userdata.quantity
                sam3 = orderdetails1.objects.get(orderid = limit.orderid)
                if side == "BUY":
                    if float(data1['price']) <= limit.price:
                        sam3.sellprice = float(data1['price'])
                        q = (float(data1['price'])*float(qty))
                        sam3.sellusdt = q
                        sam3.profit = q - float(sam3.buyusdt) - float(sam3.comission)
                        profit = q - float(sam3.buyusdt) - float(sam3.comission)
                        user5 = User.objects.get(email = sam3.owner)
                        if userdata.trade == "Future":
                            user5.future = float(user5.future) + profit + float(sam3.balance)
                        if userdata.trade == "Spot":
                            user5.spot = float(user5.spot) + profit + float(sam3.balance)
                        user5.save()
                        sam3.save()
                        userdata.delete()
                        sam4 = adminorder1.objects.filter(orderid = limit.orderid)
                        for sam5 in sam4:
                            sam5.delete()
                if side == "SELL":
                    if float(data1['price']) >= limit.price:
                        sam3.buyprice = float(data1['price'])
                        q = (float(data1['price'])*float(qty))
                        sam3.buyusdt = q
                        sam3.profit = float(sam3.sellusdt) - float(sam3.comission) - q
                        profit = float(sam3.sellusdt) - float(sam3.comission) - q
                        user5 = User.objects.get(email = sam3.owner)
                        if userdata.trade == "Future":
                            user5.future = float(user5.future) + profit + float(sam3.balance)
                        if userdata.trade == "Spot":
                            user5.spot = float(user5.spot) + profit + float(sam3.balance)
                        user5.save()
                        sam3.save()
                        userdata.delete()
                        sam4 = adminorder1.objects.filter(orderid = limit.orderid)
                        for sam5 in sam4:
                            sam5.delete()


def place2():
    sam = adminorder1.objects.filter(type="TP")
    if sam:
        for limit in sam:
            de = adminorder1.objects.filter(orderid = limit.orderid)
            try:
                sa = de.get(type = "SLIMIT")
            except:
                sa = "NA"
            try:
                ma = de.get(type = "NLIMIT")
            except:
                ma = "NA"
            if sa=="NA" and ma == "NA":
                userdata = order2.objects.get(Order_id=limit.orderid)
                symbol = userdata.Symbol
                key = "https://api.binance.com/api/v3/ticker/price?symbol="+symbol
                data1 = requests.get(key)
                data1 = data1.json()
                side = userdata.side
                qty = userdata.quantity
                sam3 = orderdetails1.objects.get(orderid = limit.orderid)
                if side == "BUY":
                    if float(data1['price']) >= limit.price:
                        sam3.sellprice = float(data1['price'])
                        q = (float(data1['price'])*float(qty))
                        sam3.sellusdt = q
                        sam3.profit = q - float(sam3.buyusdt) - float(sam3.comission)
                        profit = q - float(sam3.buyusdt) - float(sam3.comission)
                        user5 = User.objects.get(email = sam3.owner)
                        if userdata.trade == "Future":
                            user5.future = float(user5.future) + profit + float(sam3.balance)
                        if userdata.trade == "Spot":
                            user5.spot = float(user5.spot) + profit + float(sam3.balance)
                        user5.save()
                        sam3.save()
                        userdata.delete()
                        sam4 = adminorder1.objects.filter(orderid = limit.orderid)
                        for sam5 in sam4:
                            sam5.delete()
                if side == "SELL":
                    if float(data1['price']) <= limit.price:
                        sam3.buyprice = float(data1['price'])
                        q = (float(data1['price'])*float(qty))
                        sam3.buyusdt = q
                        sam3.profit = float(sam3.sellusdt) - float(sam3.comission) - q
                        profit = float(sam3.sellusdt) - float(sam3.comission) - q
                        user5 = User.objects.get(email = sam3.owner)
                        if userdata.trade == "Future":
                            user5.future = float(user5.future) + profit + float(sam3.balance)
                        if userdata.trade == "Spot":
                            user5.spot = float(user5.spot) + profit + float(sam3.balance)
                        user5.save()
                        sam3.save()
                        userdata.delete()
                        sam4 = adminorder1.objects.filter(orderid = limit.orderid)
                        for sam5 in sam4:
                            sam5.delete()


def placeorder():
    i = 0
    for i in range(0,6):
        sam = adminorder.objects.all()
        try:
            limitorders = sam.filter(type="LIMIT")
        except:
            limitorders = ""
        SLorders = sam.filter(type="SL")
        TPorders = sam.filter(type="TP")
        # trade = SLorder.trade
        # leverage = SLorder.leverage
        if limitorders:
            for limitorder in limitorders:
                trade = limitorder.trade
                leverage = limitorder.leverage
                unique = limitorder.unique
                symbol = limitorder.Symbol
                percent = float(limitorder.percentage)
                if trade == "Future":
                    key = "https://fapi.binance.com/fapi/v1/ticker/24hr?symbol="+symbol
                    data = requests.get(key)
                    data = data.json()
                else:
                    key = "https://api.binance.com/api/v1/ticker/24hr?symbol="+symbol
                    data = requests.get(key)
                    data = data.json()
                if limitorder.side == "BUY":
                    if float(data['lastPrice']) <= limitorder.Price:
                        user5 = User.objects.get(email=limitorder.Owner)
                        if user5.bot == "bot1":
                            userdata = User.objects.filter(is_classic=True)
                        if user5.bot == "bot2":
                            userdata = User.objects.filter(is_premium=True)
                        if user5.bot == "bot3":
                            userdata = User.objects.filter(is_bot3=True)
                        if user5.bot == "bot4":
                            userdata = User.objects.filter(is_bot4=True)
                        for user in userdata:
                            try:
                                api_key = user.apikey
                                api_secret = user.apisecret
                                client = Client(api_key,api_secret)
                                if trade == "Future":
                                    price1 = float(client.get_avg_price(symbol=symbol)['price'])
                                    O = pd.DataFrame(client.futures_account_balance(asset = 'USDT'))
                                    balance = float(O['withdrawAvailable'].max()) * float(percent)
                                    qty = round(((balance*10)/(price1/1000))/1000, 3)
                                    if qty >= 0.005:
                                        client.futures_change_leverage(symbol=symbol, leverage=int(leverage))
                                        order = client.futures_create_order(symbol=symbol,side=limitorder.side,type="MARKET",quantity=qty)
                                        id = int(order["orderId"])
                                        order5 = client.futures_get_order(symbol=symbol,orderId= id)
                                        p = float(order5['avgPrice'])
                                        q = float(order5['executedQty'])
                                        u = (p*q)/float(leverage)
                                        post5 = OrderDetails(Symbol=symbol,Owner=user.email, buyprice = p, buyusdt=u, leverage=int(leverage),orderid=str(order["orderId"]))
                                        post5.save()
                                        post = order1(Order_id =int(order["orderId"]),unique=unique,Symbol = order["symbol"],Owner = user.email,side = limitorder.side,Price = float(order['price']),currentprice = "message[12].price",quantity = float(order['origQty']),apikey=api_key,apisecret=api_secret)
                                        post.save()
                                if trade == "Spot":
                                    price1 = float(client.get_avg_price(symbol=symbol)['price'])
                                    o = client.get_asset_balance(asset="USDT")
                                    balance = float(o['free']) * float(percent)
                                    qty = round((balance/(price1/1000))/1000, 4)
                                    if qty >= 0.0001:
                                        order = client.create_order(symbol=symbol,side = limitorder.side,type=type,quantity=qty)
                                        id = int(order["orderId"])
                                        order5 = client.get_order(symbol=symbol,orderId= id)
                                        p = float(order['fills'][0]['price'])
                                        q = float(order5['executedQty'])
                                        t = 0
                                        for orde in order['fills']:
                                            t = t + float(orde['commission'])
                                        actualqty = float(order5['executedQty']) - t
                                        u = (p*q)/float(leverage)
                                        post5 = OrderDetails(Symbol=symbol,Owner=user.email, buyprice = p, buyusdt=u, leverage=int(leverage),orderid=str(order["orderId"]))
                                        post5.save()
                                        post = order1(Order_id =int(order["orderId"]),unique=unique,trade="Spot",Symbol = order["symbol"],Owner = user.email,side = limitorder.side,Price = float(order['price']),currentprice = "message[12].price",quantity = (round(actualqty,4)-0.0001),apikey=api_key,apisecret=api_secret)
                                        post.save()
                            except:
                                pass
                        limitorder.delete()
                if limitorder.side == "SELL":
                    if float(data['lastPrice']) >= limitorder.Price:
                        user5 = User.objects.get(email=limitorder.Owner)
                        if user5.bot == "bot1":
                            userdata = User.objects.filter(is_classic=True)
                        if user5.bot == "bot2":
                            userdata = User.objects.filter(is_premium=True)
                        if user5.bot == "bot3":
                            userdata = User.objects.filter(is_bot3=True)
                        if user5.bot == "bot4":
                            userdata = User.objects.filter(is_bot4=True)
                        for user in userdata:
                            try:
                                api_key = user.apikey
                                api_secret = user.apisecret
                                client = Client(api_key,api_secret)
                                if trade == "Future":
                                    price1 = float(client.get_avg_price(symbol=symbol)['price'])
                                    O = pd.DataFrame(client.futures_account_balance(asset = 'USDT'))
                                    balance = float(O['withdrawAvailable'].max()) * float(percent)
                                    qty = round(((balance*10)/(price1/1000))/1000, 3)
                                    if qty >= 0.005:
                                        client.futures_change_leverage(symbol=symbol, leverage=int(leverage))
                                        order = client.futures_create_order(symbol=symbol,side=limitorder.side,type="MARKET",quantity=qty)
                                        id = int(order["orderId"])
                                        order5 = client.futures_get_order(symbol=symbol,orderId= id)
                                        p = float(order5['avgPrice'])
                                        q = float(order5['executedQty'])
                                        u = (p*q)/float(leverage)
                                        post5 = OrderDetails(Symbol=symbol,Owner=user.email, sellprice = p, sellusdt=u, leverage=int(leverage),orderid=str(order["orderId"]))
                                        post5.save()
                                        post = order1(Order_id =int(order["orderId"]),unique=unique,Symbol = order["symbol"],Owner = user.email,side = limitorder.side,Price = float(order['price']),currentprice = "message[12].price",quantity = float(order['origQty']),apikey=api_key,apisecret=api_secret)
                                        post.save()
                                if trade == "Spot":
                                    price1 = float(client.get_avg_price(symbol=symbol)['price'])
                                    o = client.get_asset_balance(asset="USDT")
                                    balance = float(o['free']) * float(percent)
                                    qty = round((balance/(price1/1000))/1000, 3)
                                    if qty >= 0.005:
                                        order = client.create_order(symbol=symbol,side = limitorder.side,type=type,quantity=qty)
                                        id = int(order["orderId"])
                                        order5 = client.get_order(symbol=symbol,orderId= id)
                                        p = float(order['fills'][0]['price'])
                                        q = float(order5['executedQty'])
                                        t = 0
                                        for orde in order['fills']:
                                            t = t + float(orde['commission'])
                                        actualqty = float(order5['executedQty']) - t
                                        u = (p*q)/float(leverage)
                                        post5 = OrderDetails(Symbol=symbol,Owner=user.email, sellprice = p, sellusdt=u, leverage=int(leverage),orderid=str(order["orderId"]))
                                        post5.save()
                                        post = order1(Order_id =int(order["orderId"]),unique=unique,trade="Spot",Symbol = order["symbol"],Owner = user.email,side = limitorder.side,Price = float(order['price']),currentprice = "message[12].price",quantity = (round(actualqty,4)-0.0001),apikey=api_key,apisecret=api_secret)
                                        post.save()
                            except:
                                pass
                        limitorder.delete()
        else:
            for SLorder in SLorders:
                trade = SLorder.trade
                leverage = SLorder.leverage
                symbol=SLorder.Symbol
                if trade == "Future":
                    key = "https://fapi.binance.com/fapi/v1/ticker/24hr?symbol="+symbol
                    data = requests.get(key)
                    data = data.json()
                else:
                    key = "https://api.binance.com/api/v1/ticker/24hr?symbol="+symbol
                    data = requests.get(key)
                    data=data.json()
                unique = SLorder.unique
                print("data")
                if SLorder.side == "SELL":
                    if float(data['lastPrice']) <= SLorder.Price:
                        userdata = order1.objects.filter(unique=unique)
                        for user in userdata:
                            try:
                                api_key = user.apikey
                                api_secret = user.apisecret
                                client = Client(api_key,api_secret)
                                qty = user.quantity
                                symbol = user.Symbol
                                if trade == "Future":
                                    order = client.futures_create_order(symbol=symbol,side=SLorder.side,type="MARKET",quantity=qty)
                                    id = int(order["orderId"])
                                    order5 = client.futures_get_order(symbol=symbol,orderId= id)
                                    sam3 = OrderDetails.objects.get(orderid=user.Order_id)
                                    sam3.sellprice = float(order5['avgPrice'])
                                    q = (float(order5['avgPrice'])*float(order5['executedQty']))/float(sam3.leverage)
                                    sam3.sellusdt = q
                                    sam3.profit = q - float(sam3.buyusdt)
                                    pro = q - float(sam3.buyusdt)
                                    user4 = User.objects.get(email=user.Owner)
                                    user4.profit = float(user4.profit) + pro
                                    sam3.save()
                                    user4.save()
                                else:
                                    order = client.create_order(symbol=symbol,side=SLorder.side,type="MARKET",quantity=qty)
                                    id = int(order["orderId"])
                                    order5 = client.get_order(symbol=symbol,orderId= id)
                                    sam3 = OrderDetails.objects.get(orderid=user.Order_id)
                                    sam3.sellprice = float(order['fills'][0]['price'])
                                    q = (float(order['fills'][0]['price'])*float(order5['executedQty']))/float(sam3.leverage)
                                    sam3.sellusdt = q
                                    sam3.profit = q - float(sam3.buyusdt)
                                    pro = q - float(sam3.buyusdt)
                                    user4 = User.objects.get(email=user.Owner)
                                    user4.profit = float(user4.profit) + pro
                                    sam3.save()
                                    user4.save()
                                user.delete()
                            except:
                                pass
                        SLorder.delete()
                        Tporder2 = adminorder.objects.filter(unique = SLorder.unique)
                        TPorder = Tporder2.filter(type="TP")
                        TPorder.delete()
                if SLorder.side == "BUY":
                    if float(data['lastPrice']) >= SLorder.Price:
                        userdata = order1.objects.filter(unique=unique)
                        for user in userdata:
                            try:
                                api_key = user.apikey
                                api_secret = user.apisecret
                                client = Client(api_key,api_secret)
                                qty = user.quantity
                                symbol = user.Symbol
                                print(user.Order_id)
                                if trade == "Future":
                                    order = client.futures_create_order(symbol=symbol,side=SLorder.side,type="MARKET",quantity=qty)
                                    id = int(order["orderId"])
                                    order5 = client.futures_get_order(symbol=symbol,orderId= id)
                                    sam3 = OrderDetails.objects.get(orderid=user.Order_id)
                                    sam3.buyprice = float(order5['avgPrice'])
                                    q = (float(order5['avgPrice'])*float(order5['executedQty']))/float(sam3.leverage)
                                    sam3.buyusdt = q
                                    sam3.profit = float(sam3.sellusdt) - q
                                    pro = float(sam3.sellusdt) - q
                                    user4 = User.objects.get(email=user.Owner)
                                    user4.profit = float(user4.profit) + pro
                                    sam3.save()
                                    user4.save()
                                if trade == "Spot":
                                    order = client.create_order(symbol=symbol,side=SLorder.side,type="MARKET",quantity=qty)
                                    id = int(order["orderId"])
                                    order5 = client.get_order(symbol=symbol,orderId= id)
                                    sam3 = OrderDetails.objects.get(orderid=user.Order_id)
                                    sam3.buyprice = float(order['fills'][0]['price'])
                                    q = (float(order['fills'][0]['price'])*float(order5['executedQty']))/float(sam3.leverage)
                                    sam3.buyusdt = q
                                    sam3.profit = float(sam3.sellusdt) - q
                                    pro = float(sam3.sellusdt) - q
                                    user4 = User.objects.get(email=user.Owner)
                                    user4.profit = float(user4.profit) + pro
                                    sam3.save()
                                    user4.save()
                                user.delete()
                            except:
                                pass
                        SLorder.delete()
                        Tporder2 = adminorder.objects.filter(unique = SLorder.unique)
                        TPorder = Tporder2.filter(type="TP")
                        TPorder.delete()
            for TPorder in TPorders:
                trade = TPorder.trade
                leverage = TPorder.leverage
                symbol=TPorder.Symbol
                if TPorder.side == "SELL":
                    if float(data['lastPrice']) >= float(TPorder.Price):
                        userdata = order1.objects.filter(unique=unique)
                        for user in userdata:
                            try:
                                api_key = user.apikey
                                api_secret = user.apisecret
                                client = Client(api_key,api_secret)
                                qty = user.quantity
                                symbol = user.Symbol
                                print(qty)
                                if trade == "Future":
                                    order = client.futures_create_order(symbol=symbol,side=TPorder.side,type="MARKET",quantity=qty)
                                    id = int(order["orderId"])
                                    order5 = client.futures_get_order(symbol=symbol,orderId= id)
                                    sam3 = OrderDetails.objects.get(orderid=user.Order_id)
                                    sam3.sellprice = float(order5['avgPrice'])
                                    q = (float(order5['avgPrice'])*float(order5['executedQty']))/float(sam3.leverage)
                                    sam3.sellusdt = q
                                    sam3.profit = q - float(sam3.buyusdt)
                                    pro = q - float(sam3.buyusdt)
                                    user4 = User.objects.get(email=user.Owner)
                                    user4.profit = float(user4.profit) + pro
                                    sam3.save()
                                    user4.save()
                                if trade == "Spot":
                                    print(qty)
                                    order = client.create_order(symbol=symbol,side="SELL",type="MARKET",quantity=qty)
                                    print("sanket")
                                    id = int(order["orderId"])
                                    order5 = client.get_order(symbol=symbol,orderId= id)
                                    sam3 = OrderDetails.objects.get(orderid=user.Order_id)
                                    sam3.sellprice = float(order['fills'][0]['price'])
                                    q = (float(order['fills'][0]['price'])*float(order5['executedQty']))/float(sam3.leverage)
                                    sam3.sellusdt = q
                                    sam3.profit = q - float(sam3.buyusdt)
                                    pro = q - float(sam3.buyusdt)
                                    user4 = User.objects.get(email=user.Owner)
                                    user4.profit = float(user4.profit) + pro
                                    sam3.save()
                                    user4.save()
                                user.delete()
                            except:
                                pass
                        TPorder.delete()
                        Slorder2 = adminorder.objects.filter(unique = TPorder.unique)
                        SLorder = Slorder2.filter(type="SL")
                        SLorder.delete()
                if TPorder.side == "BUY":
                    if float(data['lastPrice']) <= TPorder.Price:
                        userdata = order1.objects.filter(unique=unique)
                        for user in userdata:
                            try:
                                api_key = user.apikey
                                api_secret = user.apisecret
                                client = Client(api_key,api_secret)
                                qty = user.quantity
                                symbol = user.Symbol
                                if trade == "Future":
                                    order = client.futures_create_order(symbol=symbol,side=TPorder.side,type="MARKET",quantity=qty)
                                    id = int(order["orderId"])
                                    order5 = client.futures_get_order(symbol=symbol,orderId= id)
                                    sam3 = OrderDetails.objects.get(orderid=user.Order_id)
                                    sam3.buyprice = float(order5['avgPrice'])
                                    q = (float(order5['avgPrice'])*float(order5['executedQty']))/float(sam3.leverage)
                                    sam3.buyusdt = q
                                    sam3.profit = float(sam3.sellusdt) - q
                                    pro = float(sam3.sellusdt) - q
                                    user4 = User.objects.get(email=user.Owner)
                                    user4.profit = float(user4.profit) + pro
                                    sam3.save()
                                    user4.save()
                                if trade == "Spot":
                                    order = client.create_order(symbol=symbol,side=TPorder.side,type="MARKET",quantity=qty)
                                    id = int(order["orderId"])
                                    order5 = client.get_order(symbol=symbol,orderId= id)
                                    sam3 = OrderDetails.objects.get(orderid=user.Order_id)
                                    sam3.buyprice = float(order['fills'][0]['price'])
                                    q = (float(order['fills'][0]['price'])*float(order5['executedQty']))/float(sam3.leverage)
                                    sam3.buyusdt = q
                                    sam3.profit = float(sam3.sellusdt) - q
                                    pro = float(sam3.sellusdt) - q
                                    user4 = User.objects.get(email=user.Owner)
                                    user4.profit = float(user4.profit) + pro
                                    sam3.save()
                                    user4.save()
                                user.delete()
                            except:
                                pass
                        Slorder2 = adminorder.objects.filter(unique = TPorder.unique)
                        SLorder = Slorder2.filter(type="SL")
                        SLorder.delete()
                        SLorder.delete()
                        TPorder.delete()
        i = i + 1
        time.sleep(10)
