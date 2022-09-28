import mysql.connector as c

mydb = c.connect(
  host="localhost",
  user="santosh",
  password="Mysql@12",
  database="pythondatabase",
  auth_plugin='mysql_native_password',
)


def checkemail2(email):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from student")
    myresult = mycursor.fetchall()
    s=set()
    for a,b,c,d in myresult:
        s.add(c)
    if email in s:
        print('--user already present please choose different user name--')
        email=input('Enter your email: ')
        checkemail2(email)
    else:
        return email