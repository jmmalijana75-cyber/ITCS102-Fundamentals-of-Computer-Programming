#basic if else 
import getpass

username = "MALIJANA"
password = "hellopo"

u = input("input USERNAME ---->") 
p = getpass.getpass("input PASSWORD --->")

if u == username:
	print(" => HELLO ", username, " <-- ")
else:
	print("--> Wrong USERNAME <-- ")

if p== password:
	print(" --> CORRECT PASSWORD <-- ")
else:
	print(" --> WRONG PASSWORD <-- ")
