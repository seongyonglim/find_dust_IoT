from flask import Flask, render_template, request

import pymysql

import json

app = Flask(__name__)

@app.route('/')
def indexes():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def id_get():  #사용자 아이디를 GET으로 받음
    db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='12345',
                                  db='data_db',
                                  charset='utf8')
    cursor = db.cursor()
    id = request.args.get('id') 
    cursor.execute('SELECT id FROM data_db.User WHERE id = %s' % id)
    row = cursor.fetchall()
    if(row == ()):
        cursor.execute( 'INSERT INTO data_db.User(ID, Coin) VALUES(%s, 0);' % id )
        db.commit()
    cursor.execute('SELECT Coin FROM User WHERE id = %s' % id)
    coin = cursor.fetchall()
    print(coin)
    db.close()
    return {"result": "success", "coin": coin[0][0]} 

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/dust_data', methods=['GET'])
def dust():
    db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='12345',
                                  db='data_db',
                                  charset='utf8')
    cursor = db.cursor()
    bounds = request.args.get('bounds')
    bounds = json.loads(bounds)
    x_res = bounds[1]
    y_res = bounds[2]
    bounds = bounds[0]
    dx = (bounds['oa'] - bounds['ha']) / 2 / x_res
    dy = (bounds['pa'] - bounds['qa']) / 2 / y_res
    data = []
    for i in range(x_res):
        _data = []
        for j in range(y_res):
            x_min = bounds['ha'] + (i * 2 * dx)
            x_max = bounds['ha'] + ((i + 1) * 2 * dx)
            y_min = bounds['qa'] + (j * 2 * dy)
            y_max = bounds['qa'] + ((j + 1) * 2 * dy)
            cursor.execute('SELECT AVG(Pullution) FROM data_db.DustData WHERE x > '+ str(x_min) +'AND x < '+ str(x_max) + 'AND y > ' + str(y_min) + 'AND y < ' + str(y_max))
            row = cursor.fetchall()
            _data.append([row[0][0], bounds['ha'] + ((i * 2 + 1) * dx), bounds['qa'] + ((j * 2 + 1) * dy)])
        data.append(_data)
    
    db.close()
    return {'data':data}

@app.route('/shop', methods=['GET'])
def shop():
    db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='12345',
                                  db='data_db',
                                  charset='utf8')
    cursor = db.cursor()
    id = request.args.get('id')
    if id is not None:
        cursor.execute('SELECT id FROM data_db.User WHERE id = ' + id)
        row = cursor.fetchall()
        if row != ():    
            return render_template('shop.html')
    db.close()
    return render_template('shop_login.html')

if __name__ == '__main__':
    app.run(debug=True)
    