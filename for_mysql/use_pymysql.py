#! /usr/bin/python3
# -*- coding : utf-8 -*-

import pymysql 

db = pymysql.connect(host = "localhost", 
                     port = 3306,
                     user = "root", 
                     password = "zijianlv", 
                     db = "test", 
                     charset='utf8')

#获取光标
cursor = db.cursor()

effect_row = cursor.execute('''
CREATE TABLE student(
    id varchar(10) NOT NULL,
    name varchar(10) NOT NULL,
    age int(10) NOT NULL DEFAULT 0,
    score int(10) NOT NULL DEFAULT 0,
    PRIMARY KEY(id)
)
''')

effect_row = cursor.execute('''INSERT INTO student VALUES 
                            ('1', 'lzj', 22, 99),
                            ('2', 'zjl', 23, 98),
                            ('3', 'wrh', 21, 80)''')
db.commit()

db.close()

