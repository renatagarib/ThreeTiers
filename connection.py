#from __future__ import print_function

hostname = 'localhost'
username = 'root'
password = 'nilmar21'
database = 'mydb'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT CPF, nome FROM aluno" )

    for cpf, nome in cur.fetchall() :
        print( cpf, nome )


print( "Using mysqlclient (MySQLdb):" )
import MySQLdb
myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

print( "Using mysql.connector:" )
import mysql.connector
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

print( "Using pymysql:" )
import pymysql
myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()