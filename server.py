from flask import Flask, render_template, request

import pymysql

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
    sw = bounds[0]
    ne = bounds[1]
    return {1:1}

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
    