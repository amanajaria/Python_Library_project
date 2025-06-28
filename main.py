import os
import platform
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()


mycursor.execute("create database if not exists aman ")

def Add_Record():
    L=[]
    pid1=int(input("Enter the parking number : "))
    L.append(pid1)
    pname1=input("Enter the Parking Name: ")
    L.append(pname1)
    level1=input("Enter level of parking : ")
    L.append(level1)
    vehicleno1=input("Enter the Vehicle Number : ")
    L.append(vehicleno1)
    
    stud=(L)
    sql="insert into parking (pid,pnm,level,vehicle_number) values (%s,%s,%s,%s)"
    mycursor.execute(sql,stud)
    mydb.commit()
def RecView():
    print("Select the search criteria : ")
    print("1. Parking Number")
    print("2. Parking Name")
    print("3. Level No")
    print("4. All")
    ch=int(input("Enter the choice : "))
    if ch==1:
        s=int(input("Enter Parking no : "))
        rl=(s,)
        sql="select * from parking where pid1=%s"
        mycursor.execute(sql,rl)
    elif ch==2:
        s=input("Enter Parking Name : ")
        rl=(s,)
        sql="select * from parking where pnm1=%s"
        mycursor.execute(sql,rl)
    elif ch==3:
        s=int(input("Enter Level of Parking : "))
        rl=(s,)
        sql="select * from parkmaster11 where level1=%s"
        mycursor.execute(sql,rl)
    elif ch==5:
        sql="select * from parking"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        print("Details about Parking are as follows : ")
        print("(Parking Id,Parking Name,Level,FreeSpace(Y/N),Vehicle No,No of days for parking,Payment)")
    for x in res:
            print(x)
def Vehicle_Detail():
    L=[]
    vid1=int(input("Enter Vehicle No : "))
    L.append(vid1)
    vnm1=input("Enter Vehicle Name/Model Name : ")
    L.append(vnm1)
    dateofpur1=input("Enter Date of purchase : ")
    L.append(dateofpur1)
    vdt=(L)
    sql="insert into vehicle (vid1,vnm1,dateofpur1) values (%s,%s,%s)"
    mycursor.execute(sql,vdt)
    mydb.commit()
def Vehicle_View():
    vid=int(input("Enter the vehicle number of the vehicle whose details is to be viewed : "))
    sql="Select parking.pid, parking.pnm, parking.level, vehicle.vid,vehicle.vnm,vehicle.dateofpur from parkmaster11,vehicle where parkmaster11.vid=vehicle.vid "
    rl=(vid,)
    mycursor.execute(sql,rl)
    res=mycursor.fetchall()
    for x in res:
        print(x)
def remove():
    vid1=int(input("Enter the vehicle number of the vehicle to be deleted : "))
    rl=(roll,)
    sql="Delete from vehicle where vid1=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
def Menu():
    print("==============M A I N     M E N U ============")
    print("\n\n\Enter 1 : To Add Parking Detail")
    print("Enter 2 : To View Parking Detail ")
    print("Enter 3 : To Add Vehicle Detail ")
    print("Enter 4 : To Remove Vehicle Record")
    print("Enter 5 : To see the details of Vehicle")
    input_dt = int(input("Please Select An Above Option: "))
    if(input_dt== 1):
        Add_Record()
    elif (input_dt==2):
        RecView()
    elif (input_dt==3):
        Vehicle_Detail()
    elif (input_dt==4):
        remove()
    elif (input_dt==5):
        Vehicle_View()
    else:
        print("Enter correct choice. . . ")
    Menu()
def runAgain():
    Menu()
    unAgn = input("\nwant To Run Again Y/n: ")
    while(unAgn.lower() == 'y'):
        if(platform.system() == "Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        

runAgn = input("\nwant To Run Again Y/n: ")
runAgain()

