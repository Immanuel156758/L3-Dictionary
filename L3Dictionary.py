Password = {"George":"1243897","Thomas":"3249782","Immanuel":"2346598"}
u = input("Enter your username:")

if(u in Password):
	p = input("Enter your password:")
	if(p == Password[u]):
		print("You are succesfully logged in")
	else:
		print("Password is")
else:
	print("Username not found")

