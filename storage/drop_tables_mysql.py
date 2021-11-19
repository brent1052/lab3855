import mysql.connector

db_conn = mysql.connector.connect(host="brent3855.eastus2.cloudapp.azure.com", user="user", 
password="password", database="events")
db_cursor = db_conn.cursor()
db_cursor.execute('''
 DROP TABLE door_motion, motion
''')
db_conn.commit()
db_conn.close()