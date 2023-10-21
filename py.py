from flask import Flask, request, render_template, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
# MySQL設定
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '0427paN-'  # 請替換成你的MySQL密碼
app.config['MYSQL_DB'] = 'TA'

mysql = MySQL(app)

# API端點：獲取所有TA資料，每個TA一行，以HTML換行符號分隔
@app.route('/ta', methods=['GET'])
def get_ta():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM TA')
    ta_data = cur.fetchall()
    cur.close()

    formatted_data = "<br>".join([f"{item[0]}, {item[1]}, {item[2]}" for item in ta_data])

    # 在這裡使用Flask的render_template可以在HTML中呈現資料
    return formatted_data

# API端點：添加新的TA資料
@app.route('/add_ta', methods=['POST'])
def add_ta():
    name = request.form.get('Name')
    email = request.form.get('Email')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO TA (NAME, EMAIL) VALUES (%s, %s)", (name, email))
    mysql.connection.commit()
    cur.close()

    return "Data has been added successfully！"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
