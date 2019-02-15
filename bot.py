from db import *



def exec(msisdn,response):
	user=getUserByNo(msisdn)

	if(user):
		print("User Exists")
		#user exists

	else:
		#user does not exist >> Create the user

		user = insertUser(name="",msisdn=msisdn,gender="",email="")
		# command=saveControlBoard(user_id=user[0],count="1")
		user = getUserByNo(msisdn)
		saveControlBoard(user_id=user[0], count="0")
	#checkcurrentSTatusin Control

	user_id=user[0]


	c=getControlBoard(user_id)
	cuurent_count=c[2]

	cancontinue = True

	saveControlBoard(user_id=user_id, count=(cuurent_count+1))
	if(response):
		saveResponse(response)
		if(cuurent_count==2):
			userName(response, msisdn)
		elif (cuurent_count==3):
			userMail(response, msisdn)
		elif (cuurent_count==4):
			userGender(response, msisdn)
			message="You are now successfully Registered; Here are your details: "

			cancontinue=False

		if(cancontinue):
			return printCommand(cuurent_count+1)
		else:
			print(message)
			print(userDetails(msisdn))



