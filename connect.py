import pymysql



conn = pymysql.connect(host='127.0.0.1',port =3306,user='root',passwd='1558785107zsh',db='pythonservice',charset='utf8')
cursor =conn.cursor()

effect_row = cursor.execute("select * from emp")


date =[
    ('金角','女','10041','1009','1','2014-05-09', '2018-01-12'),
('银角','男','10042','1010','8','2014-05-04', '2018-08-12')
]
print(effect_row)
#print(cursor.fetchone())
print(cursor.fetchall())
cursor.executemany("insert into emp(ename,sex,salary,deptid,leaderid,birdate,income)"
                   " values (%s,%s,%s,%s,%s,%s,%s)",date)
conn.commit()