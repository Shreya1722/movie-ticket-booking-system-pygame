import mysql.connector as sql
con = sql.connect(host = "localhost" , user = "root" , password = "veda_22bhyala", database = "_Cinema_")
if con.is_connected:
    cur = con.cursor()
    cur.execute("CREATE TABLE if not exists MOVIES (Movie_Name text);")
    cur.execute("INSERT INTO MOVIES values('Leo');")
    cur.execute("INSERT INTO MOVIES values('Hostel Hudugaru Bekagiddare');")
    cur.execute("INSERT INTO MOVIES values('Sirf Ek Banda Khafi Hai');")
    cur.execute("INSERT INTO MOVIES values('Hi Nanna');")
    cur.execute("INSERT INTO MOVIES values('2018');")
    cur.execute("INSERT INTO MOVIES values('The Menu');")
    con.commit()
