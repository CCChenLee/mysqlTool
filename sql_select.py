#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import pymysql

def query_data():
	#打开数据库连接
	db=pymysql.connect("localhost","root","123456","xinku")
	#使用cursor()方法获取操作游标
	cursor=db.cursor()
	#SQL查询语句
	sql="SELECT * FROM EMPLOYEE WHERE INCOME > %d" % 10000
	try:
		#执行SQL语句
		cursor.execute(sql)
		#获取所有记录列表
		results=cursor.fetchall()
		for row in results:
			fname=row[0]
			lname=row[1]
			age=row[2]
			sex=row[3]
			income=row[4]
			create_time=row[5]
			#输出结果
			print("first_name=%s,last_name=%s,age=%d,sex=%s,\n"
					"income=%d,create_time=%s"%(fname,lname,
						age,sex,income,create_time))
	except Exception as e:
		print("Error:unable to fecth data.Error info:%s"%e)
	finally:
		#记得关闭数据库
		db.close()
def main():
	query_data()

if __name__=="__main__":
	main()