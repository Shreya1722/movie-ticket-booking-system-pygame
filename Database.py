import mysql.connector as sql
con = sql.connect(host = "localhost" , user = "root" , password = "123",database="_Cinema_")

if con.is_connected:
    cur = con.cursor()
    cur.execute("CREATE TABLE if not exists Cinema (Movie text,Ticket int,Phone_no varchar(10));")
    con.commit()
    cur.execute("CREATE TABLE if not exists MOVIES (Movie_Name text);")
    cur.execute("INSERT INTO MOVIES values('Viduthalai');")
    cur.execute("INSERT INTO MOVIES values('Hostel Hudugaru Bekagiddare');")
    cur.execute("INT INTO MOVIES values('Dasara');")
    cur.execute("INSERT INTO MOVIES values('2018');")
    cur.execute("INSERT INTO MOVIES values('The Menu');")
    con.commit()
    cur.execute("CREATE TABLE if not exists Tickets (No_of_Tickets int);")
    cur.execute("insert into tickets values(180);")
    con.commit()
