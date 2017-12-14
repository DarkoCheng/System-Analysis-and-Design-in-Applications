#!/usr/bin/python3

import pymysql.cursors
import time
import sys

db = pymysql.connect("localhost","grant","testing","development", charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()

def insert(message, id1):
    currTime = time.strftime("%H:%M:%S", time.gmtime())
    currTime1 = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    sql = """INSERT INTO messages(message_id, message, time, createdAt, updatedAt) VALUES (%s, %s, %s, %s, %s)"""
    try:
        cursor.execute(sql, (int(id1), message, currTime, currTime1, currTime1))
        db.commit()
    except pymysql.MySQLError as e:
        print ("Rolling back bad info:" ,e)
        db.rollback()

def searchMessage_id(id1):
    sql = "SELECT * FROM messages WHERE message_id = %s"
    try:
        cursor.execute(sql, id1)
        results = cursor.fetchall()
        for row in results:
            print (row)
    except pymysql.MySQLError as e:
        print ("Error: unable to fetch data:", e)

def delete(id1):
    sql = "DELETE FROM messages WHERE message_id = %s"
    try:
        cursor.execute(sql, id1)
        db.commit()
    except pymysql.MySQLError as e:
        print ("Rolling back bad info:" ,e)
        db.rollback()

def update(id1, str1):
    sql = "UPDATE messages SET message = %s WHERE message_id = %s"
    try:
        cursor.execute(sql, (str1, id1))
        db.commit()
    except pymysql.MySQLError as e:
        print ("Error: unable to fetch data:", e)


if __name__=="__main__":
    if sys.argv[1] == "insert":
        insert(sys.argv[2], sys.argv[3]) #hard coded time, createAt and updateAt
    elif sys.argv[1] == "search":
        searchMessage_id(sys.argv[2]) #search by id
    elif sys.argv[1] == "delete":
        delete(sys.argv[2])
    elif sys.argv[1] == "update":
        update(sys.argv[2], sys.argv[3])
