#! /usr/bin/python3
# -*- coding : utf-8 -*-

import sys
import pymysql as pydb

db = pydb.connect(host = "localhost", 
                  port = 3306,
                  user = "root", 
                  password = "zijianlv", 
                  db = "test", 
                  charset='utf8')

cursor = db.cursor()

sql = "SELECT * from test.student"
effect_row = cursor.execute(sql)

result_one = cursor.fetchone()
print(result_one)

cursor.scroll(-1, mode='relative')
result_two = cursor.fetchmany(2)    
print(result_two)

cursor.scroll(-2, mode='relative')
result_all = cursor.fetchall() 
with open("./test.txt", "wt") as f:
    it = iter(result_all)
    for x in it:
        for y in x:
        print(y, file = f)

cursor.close()
db.close()
