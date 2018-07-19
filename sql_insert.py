#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import pymysql
import datetime

def insert_record():
	#打开数据库连接
	db=pymysql.connect("localhost","root","123456","xinku")
	#使用cursor()方法获取操作游标
	cursor=db.cursor()
	#SQL插入语句
	sql="INSERT INTO EMPLOYEE"\
		"(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME,CREATE_TIME)"\
		"VALUE('%s','%s',%d,'%c',%d,'%s')"\
		%('mei','qi',26,'G',888.00,datetime.datetime.now())
	try:
		#执行SQL语句
		cursor.execute(sql)
		#提交到数据库执行
		db.commit()
		print("INSERT SUCCESS.")
	except Exception as e:
		print('INSERT INTO MySQL table failed. Case:%s'%e)
		#如果发生错误就回滚
		db.rollback()
	finally:
		#记得关闭数据库连接
		db.close()

def main():
	insert_record()

if __name__=="__main__":
	main()