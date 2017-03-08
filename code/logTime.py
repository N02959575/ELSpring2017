#!/usr/bin/python
import time
import sqlite3 as mydb

"""Log Current Date and Time
  Returns a list [date, time]"""

def readTime():
	#Date
	xdate = time.strftime("%Y-%m-%d")
	#Time(24 hour)
	xtime = time.strftime("%H:%M:%S")
	return [xdate, xtime]

def logTime():
 	con = mydb.connect('/home/pi/ELSpring2017/code/testTime.db')
 	with con:
 		try:
			#Get list from readTime() function
 			[d, t]=readTime()
			#Prints current date and time
 			print readTime()
			#Assign con.cursor to cur
 			cur = con.cursor()
 			#Inserts values to database, into the Time table
 			cur.execute('insert into Time values(?,?)', (d, t))
 			print "Date and Time logged"
 		except:
 			print "Error!!"
logTime()