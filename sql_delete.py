#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import pymysql

def delete_record():
	#打开数据库连接
	db=pymysql.connect("localhost","root","123456","xinku")
	#使用cursor()方法获取操作游标
	cursor=db.cursor()
	#SQL删除语句
	sql="DELETE FROM EMPLOYEE WHERE AGE > %d"%25
	try:
		#执行SQL语句
		cursor.execute(sql)
		#提交到数据库执行
		db.commit()
		print('DELETE SUCCESS.')
	except Exception as e:
		print("DELETE RECORD FAILED. CASE:%s"%e)
		#发生错误时回滚
		db.rollback()
	finally:
		#关闭连接
		db.close()

def main():
	delete_record()

if __name__=="__main__":
	main()