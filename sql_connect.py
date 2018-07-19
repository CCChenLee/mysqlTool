#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import pymysql

def db_connect():
	#打开数据库连接
	db=pymysql.connect("localhost","root","123456")
	#使用cursor()方法创建一个游标对象cursor
	cursor=db.cursor()
	#创建数据库
	cursor.execute("CREATE DATABASE xinku")
	#使用execute()方法执行SQL查询
	cursor.execute("SELECT VERSION()")
	#使用fetchone()方法获取单条数据
	data=cursor.fetchone()

	print("Database version:%s"%data)

	#关闭数据库连接
	db.close()

def main():
	db_connect()
if __name__=="__main__":
	main()