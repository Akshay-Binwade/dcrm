import pymysql.cursors

connection = pymysql.connect(user='root', password='root', host='localhost', cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

cursor.execute('CREATE DATABASE CRM')

connection.commit()

print("Done...!!!")