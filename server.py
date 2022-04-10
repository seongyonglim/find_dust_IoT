from flask import Flask, render_template, request

import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='12345',
                                  db='data_db',
                                  charset='utf8')
        self.cursor= self.db.cursor(pymysql.cursors.DictCursor)
        
    def execute(self, query, args={}):
        self.cursor.execute(query, args) 
 
    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row= self.cursor.fetchone()
        return row
 
    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row= self.cursor.fetchall()
        return row
 
    def commit():
        self.db.commit()

db = Database()
app = Flask(__name__)

@app.route('/')
def indexes():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def id_get():  #사용자 아이디를 GET으로 받음
    id = request.args.get('id') 
    row = db.executeAll('SELECT id FROM data_db.User WHERE id = ' + id)
    if(row == ()):
        db.execute('INSERT INTO data_db.User(ID, Coin) VALUES('+id+',0);')
        #db.commit()
    
    return {"result": "success"} 

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/shop')
def shop():
    return render_template('shop_login.html')

if __name__ == '__main__':
    app.run(debug=True)
    