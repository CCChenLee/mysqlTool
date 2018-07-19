#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import pymysql

def update_table():
	#打开数据库连接
	db=pymysql.connect("localhost","root","123456","xinku")
	#使用cursor()方法获取操作游标
	cursor=db.cursor()
	#SQL更新语句
	sql="UPDATE EMPLOYEE SET AGE=AGE+1 WHERE SEX='%s'"%'M'
	try:
		#执行SQL语句
		cursor.execute(sql)
		#提交到数据库执行
		db.commit()
		print("UPDATE SUCCESS.")
	except Exception as e:
		print('UPDATE MySQL table failed. Case:%s'%e)
		#发生错误时回滚
	finally:
		#记得关闭数据库
		db.close()

def main():
	update_table()

if __name__=="__main__":
	main()