#!/usr/bin/python
import os
import schedule
import time
import sqlite3 as mydb
import sys

"""Log Current Time, Temperature in Celsius and Fahrenheit
  Returns a list [time, tempC, tempF]"""

def readTemp():
	tempfile = open("/sys/bus/w1/devices/28-031689e386ff/w1_slave")
	tempfile_text = tempfile.read()
	currentTime = time.strftime('%x %X %Z')
	tempfile.close()
	tempC = float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	tempF = tempC*9.0/5.0+32.0
	return [currentTime, tempC, tempF]

def logTemp():
 	con = mydb.connect('/home/pi/ELSpring2017/code/temperature.db')
 	with con:
 		try:
 			[t,C,F]=readTemp()
			print "Current temperature is: %s F" %F
 			cur = con.cursor()
 			#sql = "insert into TempData values(?,?,?)"
 			cur.execute('insert into TempData values(?,?,?)', (t,C,F))
 			print "Temperature logged"
 		except:
			print "Error!!"
#makes the function logTemp() run every 30 seconds
schedule.every(30).seconds.do(logTemp)

#Runs Program for 10 minutes + 1 second so it can run the code one last time
t_end = time.time() + 60 * 10
while time.time() < t_end + 1:
    schedule.run_pending()
    time.sleep(1)
