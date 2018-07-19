#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import pymysql

def create_table():
	#打开数据库连接
	db=pymysql.connect("localhost","root","123456","xinku")
	#使用cursor()方法创建一个游标对象cursor
	cursor=db.cursor()
	#使用execute()方法执行SQL，如果表存在就删除
	cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
	#使用预处理语句创建表
	sql="""CREATE TABLE EMPLOYEE(
			FIRST_NAME CHAR(20)NOT NULL,
			LAST_NAME CHAR(20),
			AGE INT,
			SEX CHAR(1),
			INCOME DOUBLE,
			CREATE_TIME DATETIME)"""
	try:
		cursor.execute(sql)
		print("CREATE TABE SUCCESS.")
	except Exception as e:
		print("CREATE TABLE FAILED,CASE:%s"%e)
	finally:
		#记得关闭数据库连接
		db.close()
def main():
	create_table()

if __name__=="__main__":
	main()