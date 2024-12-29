#create database mentormanagement;
#create table student(id varchar(250),name,email varchar(250),password varchar(250));
# create table mentor(id varchar(250),name varchar(250),email varchar(250),password varchar(250));
# create table parent(id varchar(250),name varchar(250),email varchar(250),password varchar(250));
#create table studentdata(id varchar(250),name varchar(250),cgpa varchar(25),attendence varchar(250));
# create table studentremarks(id varchar(250),comment varchar(250));
# create table studentquery(id varchar(250),query varchar(250));
#create table assign(studentid varchar(250),mentorid varchar(250));
import mysql.connector
from mysql.connector import Error
import string
import random
import base64
def db_connection():
            try:
                connection = mysql.connector.connect(host='localhost',
                                                     database='mentormanagement',
                                                     user='root',
                                                     password='admin')
                if connection.is_connected():
                    db_Info = connection.get_server_info()
                    print("Connected to MySQL Server version ", db_Info)
                    cur = connection.cursor()
                    return connection,cur
            except Error as e:
                print(e)
#db_connection()
def studentregister(name,username ,password):
    N = 6

    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
    connection,cur=db_connection()
    query=("insert into student(id ,name,email,password) values(%s,%s,%s,%s)" )
    cur.execute(query,(res ,name,username ,password))
    connection.commit()
#studentregister("naveen@gmail.com" ,"6305416114")
def parentregister(id,name,username ,password):
    connection,cur=db_connection()
    query=("insert into parent(id,name,email,password) values(%s,%s,%s,%s)" )
    cur.execute(query,(id,name,username ,password))
    connection.commit()
#parentregister('Q4T6UB',"rajeshrao@gmail.com" ,"987654")
def mentorregister(name,username ,password):
    N = 6

    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
    connection,cur=db_connection()
    query=("insert into mentor(id ,name,email,password) values(%s,%s,%s,%s)" )
    cur.execute(query,(res ,name,username ,password))
    connection.commit()
#mentorregister("srinu@gmail.com" ,"456321")

def comments(id,comment):

    connection,cur=db_connection()
    query=("insert into studentremarks(id ,comment) values(%s,%s)" )
    cur.execute(query,(id,comment))
    connection.commit()
#comments("Q4T6UB" ,"your child have low attendence  percentage")

def studentquery(id,q):

    connection,cur=db_connection()
    query=("insert into studentquery(id ,query) values(%s,%s)" )
    cur.execute(query,(id,q))
    connection.commit()
#studentquery("srinu@gmail.com" ,"wrong cgpa,please update it")

def student_data(id,name,cgpa,attendence):

    connection,cur=db_connection()
    query=("insert into studentdata(id,name,cgpa,attendence) values(%s,%s,%s,%s)" )
    cur.execute(query,(id,name,cgpa,attendence))
    connection.commit()
#student_data("Q4T6UB","naveen","6.3","89%")

def retrivestudentandmentor():
    connection,cur=db_connection()
    cur.execute("select id from student")
    data1=cur.fetchall()
    sid=[]
    for i in  data1:
        sid.append(i[0])
    cur.execute("select id from mentor")
    data2=cur.fetchall()
    mid=[]
    for i in  data2:
        mid.append(i[0])
    return sid,mid
#()
def assign(sid,mid):
    #sid,mid=retrivestudentandmentor()
    connection,cur=db_connection()
    query=("insert into assign(studentid ,mentorid) values(%s,%s)" )
    for i in sid:
        cur.execute(query,(i,mid))
        connection.commit()
#assign()
def sretrieve():
    connection,cur=db_connection()
    cur.execute("select studentid from assign")
    data=cur.fetchall()
    studentid=[]
    for i in data:
        studentid.append(i[0])
    return studentid
def rdata(id):
    connection,cur=db_connection()
    cur.execute("select * from studentdata where id=%s",(id,))
    data=cur.fetchall()
    n=[]
    c=[]
    a=[]
    for i in data:
        n.append(i[1])
        c.append(i[2])
        a.append(i[3])
    return n,c,a
def updatedata(name,cgpa,percentage,id):
    connection,cur=db_connection()
    cur.execute("update studentdata set name=%s,cgpa=%s,attendence=%s where id =%s",(name,cgpa,percentage,id))
    connection.commit()

def deletedata(id):
    connection,cur=db_connection()
    cur.execute("delete from studentdata where id=%s",(id,))
    connection.commit()

def respquery(id,query):
    connection,cur=db_connection()
    cur.execute("insert into studentquery(id,query) values(%s,%s)",(id,query))
    connection.commit()

def sretrieve1():
    connection,cur=db_connection()
    cur.execute("select id from studentdata")
    data=cur.fetchall()
    studentid=[]
    for i in data:
        studentid.append(i[0])
    print(studentid)
    return studentid
#sretrieve1()
def sretrieve2():
    connection,cur=db_connection()
    cur.execute("select id from mentor")
    data=cur.fetchall()
    mentorid=[]
    for i in data:
        mentorid.append(i[0])
    return mentorid
def retrieveassign():
    connection,cur=db_connection()
    cur.execute("select * from assign")
    data=cur.fetchall()
    studentid=[]
    for i in data:
        studentid.append(i)

    #print(studentid)
    return studentid
#retrieveassign()
def retrieveassign2():
    connection,cur=db_connection()
    d=retrieveassign()
    d1=[list(ele) for ele in d]
    for k in d1:
        cur.execute("select name from student where id=%s",(k[0],))
        data=cur.fetchall()
        cur.execute("select name from  mentor where id=%s",(k[1],))
        data1=cur.fetchall()
        
        for i,j in zip(data,data1):
            k.insert(1,i[0])
            k.insert(3,j[0])
    return d1
#retrieveassign2()
