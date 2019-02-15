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
	data=cursor.execute("select * from users where msisdn=%s" % (msisdn))
	return cursor.fetchone()

def getCommand(count):
	db=connect()
	cursor=db.cursor()
	data=cursor.execute("select * from commands where id=%s" % (count))
	return cursor.fetchone()

def insertUser(name,msisdn,gender,email):

		db=connect()
		cursor = db.cursor()
		cursor.execute('INSERT INTO users (name, email, msisdn, gender) VALUES ("%s", "%s", "%s", "%s")' % (
		name, email, msisdn, gender))  # Commit your changes in the database
		# cursor.execute('INSERT INTO control_board (msisdn, count) values ("%s", 1)' % (msisdn))
		db.commit()
		cursor =db.cursor()



def printCommand(commandId):
	db = connect()
	cursor = db.cursor()
	cursor.execute("select * from commands where id = %s" % (commandId))
	return cursor.fetchone()

def getControlBoard(user_id):
	db = connect()
	cursor = db.cursor()
	cursor.execute("select * from control_board where user_id = %s order  by `count` desc limit 1" % (user_id))
	return cursor.fetchone()


def saveControlBoard(user_id,count):
	db = connect()
	cursor = db.cursor()
	cursor.execute('INSERT INTO control_board (`user_id`,`count`) VALUES ("%s", "%s")' % (
		user_id, count))  # Commit your changes in the database
	# cursor.execute('INSERT INTO control_board (msisdn, count) values ("%s", 1)' % (msisdn))
	db.commit()

	return []

def saveResponse(message):
	db = connect()
	cursor = db.cursor()
	cursor.execute('INSERT INTO responses (response_text) values ("%s")' % (message))
	db.commit()

def userName(name, phone):
	db = connect()
	cursor = db.cursor()
	sql = "UPDATE users SET  name = '%s' WHERE msisdn = '%s'" % (name, phone)
	cursor.execute(sql)
	db.commit()

def userMail(mail, phone):
	db = connect()
	cursor = db.cursor()
	sql = "UPDATE users SET  email = '%s' WHERE msisdn = '%s'" % (mail, phone)
	cursor.execute(sql)
	db.commit()

def userGender(gender, phone):
	db = connect()
	cursor = db.cursor()
	sql = "UPDATE users SET  gender = '%s' WHERE msisdn = '%s'" % (gender, phone)
	cursor.execute(sql)
	db.commit()
def userDetails(msisdn):
	details = getUserByNo(msisdn)

	stre="\tYou name: %s\n\tEmail: %s\n\tGender: %s\n\tphone no: %s\n"% (details[1], details[2], details[4], details[3])

	return stre
