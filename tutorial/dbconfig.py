# import psycopg2
import pymysql

hostname = '111.231.64.142'
username = 'root'
password = 'xy520tgp'  # your password
database = 'aidang'
charset = 'utf8mb4'
connection = pymysql.connect(
    host=hostname, user=username, password=password,
    db=database, charset=charset, cursorclass=pymysql.cursors.DictCursor
)
