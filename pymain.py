#!/usr/bin/python
# -*- coding:utf-8 -*-
from cmath import sqrt
from curses import doupdate
from datetime import datetime
import http.server
from pydoc_data import topics
import socketserver
import cgi
import cgitb
import os
from syslog import LOG_LOCAL3
from xmlrpc.client import DateTime
import mysql.connector
import time

class session:
    def _init_(self, usrname, usrpw, time):
        self.usrname = usrname
        self.usrpw = usrpw
        self.strttime = time
        self.client_IP = socketserver.get_request()
        self.usrSesprot = "/<logON"+ " " + str(self.client_IP) + datetime.date + " " + time.time() + " " + ">"
        return file2Str("main.html").format(**locals()), self.usrSesprot

class database:
    def getValue(self, Value, where, rowid):
        self.execute = "SELECT " + rowid + "FROM" + self + "WHERE id = " + where, Value; 
        dbvalue = self.cursor()
        return dbvalue

    def setValue(self, Value, where, rowid):
        self.execute = "UPDATE" + rowid + "FROM" + self + "WHERE id = " + where, Value;

    def insertTopic(self, name, enviorment, checks):
        self.execute = "INSERT INTO topics (name, enviorment, checks)Values(%("+ name + ")s, %(" + enviorment + ")s, %(" + checks +")s"
                        
    def insertUser(self, name, adress, username, userpw, checks):
        self.execute = "INSERT INTO user (name, adress, username, userpw, checks)Values(%("+ name +")s, %("+ adress +")s, %("+ username + ")s, %("+ userpw +")s, %("+ checks +")s)"
        checksum = self.coursor()
        if checksum == [name, adress, username, userpw, checks]:
            return
        else:
            print("something wrong in ur database")

    def updateUser(self, name, adress, username, userpw, checks):
        update = [name, adress, username, userpw, checks]
        self.execute = "Select" + name + "FROM" + self;
        for  i in self.cursor():
            if self.Cursor([i]) != update[i]:
                self.updateUser(update[i])
        print("Update done !")

    def deleteTopic(self, topicname):
        self.execute = "DELETE FROM" + self + "WHERE" + topicname 

    def deleteUser(self, username):
        self.execute(self, username)


def main():

    #Start Servertime and logwriting
    start = int(time.time())
    cgitb.enable(display=0, logdir="/path/to/logdir")

    try:
        #set on SQL Connectons
        IACUser = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword"
    )

        IACTopics = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword"
    )
    except:
        print("NO Connection 2  SQL-Databases")
        usercursor.execute("Create Table user (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), adress VARCHAR(255), usrnme VARCHAR(255), usrpw VARCHAR(255), check INT, usrprot VARCHAR(255)")
        topiccursor.execute("Create Taple topics (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), envirment VARCHAR(255), check INT)")

    print( time.time + "Databases OK")

    #First Contect ;)
    PORT = 8080
    Handler = http.server.SimpleHTTPRequestHandler(directory="/main.html")

    #further settings for SQL Interactions or enables the tablerequest
    usercursor = IACUser.cursor()
    topiccursor = IACTopics.cursor()

    #TCP/IP Connection
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
    httpd.serve_forever

    print(time.time + "Server online starting service")
    
    

    # adds checks from formula 2 database and closes vote in html
    # within User Session protocol
def vote(usrcheck, topcheck,poscheck, form, usrSesport):   
    postID = form.submit
    if form.check == True:
        poscheck = poscheck +1;
        usrSesport = usrSesport + "</vote" + postID + "check" + " " + DateTime.date() + " " + time.time() +"  /" 

    if form.bait == True:
        check = check + 1;
        usrcheck = usrcheck + 1;
        usrSesport = usrSesport + time.time + "</vote" + postID + "check" + ">" 

    if form.hype == True:
        check = check + 1;
        topcheck = topcheck + 1;
        usrSesport = usrSesport + time.time + "</vote" + postID + "check" + ">" 

    # insert SQL Eventflag Timestamp
    return file2Str("voteclosing.html").format(**locals()), usrSesport

#opens files 2 add or choose html files
def file2Str(fname):
    try:
        f = fname.open()
        content = f.read()
        return content
    except:
        return "No file found/counld´t open \n"

def addTopic(usrSesprot):    ##adds Topic in database
    form = cgi.FieldStorage()
    post_id = form.submit
    topics.insertTopic(form.name,form.enviorment,form.checks)
    usrSesprot = usrSesprot + "</addTopic" + " " + form.name + " " + datetime.date + " " + time.time + " >"
    return file2Str("addtopic.html").format(**locals()), usrSesprot

def addUser(usrSesprot):    ##adds User to database
    form = cgi.FieldStorage()
    post_id = form.submit
    user.insertUser(form.name, form.adress, form.username, form.userpw, form.checks)
    usrSesprot = usrSesprot + "</addUser" + " " + form.username + " " + datetime.date + " " + time.time + " >"
    return file2Str("adduser.html").format(**locals()), usrSesprot


# adds comment 2 database 
def comm(primekey_id, usrSesprot):
    form = cgi.FieldStorage()
    # Uploaded writings or pictures are storaded on HDD, here creating a number for recall
    # Within return HTML content and User Session Protocoll 
    usrcomm = form.getValue("comment")
    itnbr = topics.getValue(id)
    envior = topics.getValue(primekey_id)
    delta_envoir = envior +  "</comm" + str(itnbr) + " " + DateTime.date() + " " + time.time() +"  >" 
    topics.setValue(primekey_id, delta_envoir)
    topiccont = open("val",'w')
    topiccont.write(usrcomm)
    topiccont.close()
    usrSesprot = usrSesprot + "</comm" + str(itnbr) + " " + DateTime.date() + " " + time.time() +"  >" 
    return file2Str("comments.html").format(**locals()), usrSesprot

def prot2time(protocol, arg, t_from, t_to):    ## arg to set time least, first , 5 or between 
    if arg == "least":
        prot_f = os.fopen(protocol)
        while readed_line != "":
            readed_line = prot_f.os.readline()
            n = n + 1
        for i in range(n):
            line = prot_f.os.readline()
        slc_from = line.os.rfind(" ")
        slc_to = len(line) - 3
        return line[slc_from:slc_to]

    elif arg == "first":
        prot_f = os.fopen(protocol)
        line = prot_f.os.readline()
        slc_from = line.os.rfind(" ")
        slc_to = len(line) - 3
        return line[slc_from:slc_to]

    elif arg != 0:
        prot_f = os.fopen(protocol)
        while readed_line != "":
            readed_line = prot_f.os.readline()
            n = n + 1
        if n > arg:
            
            for i in range(arg):
                line = prot_f.os.readline()
            slc_from = line.os.rfind(" ")
            slc_to = len(line) - 3
            return line[slc_from:slc_to]

    elif arg == "between":
        prot_f = os.fopen(protocol)
        list_prot_f = prot_f.os.splitlines()
        for i in range(len(list_prot_f)):
            line = list_prot_f[i]
            mrk_bd = line.os.rfind(" ")
            mrk_fd = len(line) - 3
            time = line[mrk_bd : mrk_fd]
            relation_frt_dte = 9999, 12, 31, 24, 60, 60, 1000000
            relation_snd_dte = 9999, 12, 31, 24, 60, 60, 1000000
            if relation_frt_dte.year > time_relation.year(t_from, time):                    ##fucking rabbithole these dates ;)
                relation_frt_dte.year = time_relation.year(t_from, time)
            if relation_frt_dte.year == time_relation.year(t_from, time) and relation_frt_dte.mouth > time_relation.mouth(t_from, time):
                relation_frt_dte.year = time_relation.year(t_from, time)
            if relation_frt_dte.year == time_relation.year(t_from, time) and relation_frt_dte.mouth == time_relation.mouth(t_from, time) and relation_frt_dte.day > time_relation.day(t_from, time):
                relation_frt_dte.year = time_relation.year(t_from, time)
            if relation_frt_dte.year == time_relation.year(t_from, time) and relation_frt_dte.mouth == time_relation.mouth(t_from, time) and relation_frt_dte.day == time_relation.day(t_from, time) and relation_frt_dte.hour > time_relation.hour(t_from, time):
               relation_frt_dte.year = time_relation.year(t_from, time) 
            if relation_frt_dte.year == time_relation.year(t_from, time) and relation_frt_dte.mouth == time_relation.mouth(t_from, time) and relation_frt_dte.day == time_relation.day(t_from, time) and relation_frt_dte.hour == time_relation.hour(t_from, time) and relation_frt_dte.minute > time_relation.minute(t_from, time):
               relation_frt_dte.year = time_relation.year(t_from, time)   



def time_relation(first_date, second_date):
    relation_year = second_date.year - first_date.year
    if first_date.mouth < second_date.mouth:
        relation_mouth = second_date.mouth - first_date.mouth
    else:
        abs(second_date.mouth - first_date.mouth)
        relation_year = relation_year - 1
    if first_date.day < second_date.day:
        relation_day = second_date.day - first_date.day
    else:
        abs(second_date.day - first_date.day)
        relation_mouth = relation_mouth - 1
    if first_date.hour < second_date.hour:
        relation_hour = second_date.hour - first_date.hour
    else:
        abs(second_date.hour - first_date.hour)
        relation_day = relation_day - 1
    if first_date.minute < second_date.minute:
        relation_minute = second_date.minute - first_date.minute
    else:
        abs(second_date.minute - first_date.minute)
        relation_minute = relation_minute - 1
    if first_date.second < second_date.second:
        relation_second = second_date.second - first_date.second
    else:
        abs(second_date.second - first_date.second)
        relation_second = relation_second - 1
    if first_date.microsecond < second_date.microsecond:
        relation_microsecond = second_date.microsecond - first_date.microsecond
    else:
        abs(second_date.microsecond - first_date.microsecond)
        relation_microsecond = relation_microsecond - 1
    relation_time = relation_year, relation_mouth, relation_day, relation_hour, relation_minute, relation_second, relation_microsecond

    return relation_time









def prot2act():




def feedgenerator(Session):
    # t_from sets leats time for watching back !!
    t_to = datetime.date 

##########FILEUPLOAD##############
# Get filename here.
#fileitem = form['filename']

# Test if the file was uploaded
#if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
#   fn = os.path.basename(fileitem.filename)
#   open('/tmp/' + fn, 'wb').write(fileitem.file.read())

#   message = 'The file "' + fn + '" was uploaded successfully'
   
#else:
#   message = 'No file was uploaded'
   
#print """


