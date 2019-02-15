import pymysql


def connect():
	db = pymysql.connect("localhost", "xyz", "12344321", "ChukaCu")
	return db

def getUsers():
	db=connect()
	cursor=db.cursor()
	data=cursor.execute("select * from users")
	return cursor.fetchall()


def getUserByNo(msisdn):
	db=connect()
	cursor=db.cursor()
	data = cursor.execute("select * from users where msisdn=%s" % (msisdn))
	return cursor.fetchone()






#s=getUsers()

#for user in s:
#	print(user)

print(getUsers())
print(getUserByNo("0705126328"))	

