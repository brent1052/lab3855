import mysql.connector



db_conn = mysql.connector.connect(host="brent3855.eastus2.cloudapp.azure.com", user="root", 
password="password", database="events")

db_cursor = db_conn.cursor()
db_cursor.execute('''
 CREATE TABLE door_motion
 (id INT NOT NULL AUTO_INCREMENT,
 location VARCHAR(250) NOT NULL,
 item VARCHAR(250) NOT NULL,
 time  VARCHAR(250) NOT NULL,
 state VARCHAR(250) NOT NULL,
 date_created VARCHAR(100) NOT NULL,
 CONSTRAINT door_motion_pk PRIMARY KEY (id))
 ''')
db_cursor.execute('''
 CREATE TABLE motion
 (id INT NOT NULL AUTO_INCREMENT,
  location VARCHAR(250) NOT NULL,
  item VARCHAR(250) NOT NULL,
  time VARCHAR(250) NOT NULL,
  action VARCHAR(250) NOT NULL,
  date_created VARCHAR(100) NOT NULL,
  CONSTRAINT motion_pk PRIMARY KEY (id))
 ''')


db_conn.commit()
db_conn.close()
