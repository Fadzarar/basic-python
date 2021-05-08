semua_email = []
file = open("mailist.txt", "r")
for email in file:
	semua_email.append(email)
file.close()
print(semua_email)
email_bersih = []

for i in semua_email:
	bersih = i.replace("\n","")
	email_bersih.append(bersih)
print(email_bersih)