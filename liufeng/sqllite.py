#!/usr/bin/python3

# @author liu-feng
# @email w710989327@foxmail.com
# @time 2018/1/8 16:34
import json
import sqlite3

__author__ = 'liu-feng'
__email__ = 'w710989327@foxmail.com'

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS user (id INT(11) PRIMARY KEY ,name VARCHAR(20))')
# cursor.execute('INSERT INTO user (id,name) VALUES(1,\'liufeng\')')
# cursor.execute('INSERT INTO user (id,name) VALUES(2,\'zhangsan\')')
# cursor.execute('INSERT INTO user (id,name) VALUES(3,\'lisi\')')

print(cursor.rowcount)

# cursor.close()

conn.commit()

# conn.close()


cursor.execute('SELECT * FROM user WHERE id > ?', (1,))

values = cursor.fetchall()

print(json.dumps(values))

cursor.close()

conn.close()
