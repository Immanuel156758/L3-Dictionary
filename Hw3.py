capitals = {}
while True:
	print("1. Insert\n2. Display all countries\n3. Display all capitals\n4. Get capital\n5. Delete\n6. Exit")
	num = int(input("Choose a number"))

	if(num == 1):
		name1 = input("What is the country's name?")
		name2 = input("What is the capital's name?")
		capitals[name1] = name2

	elif(num == 2):
		print(list(capitals.keys()))

	elif(num == 3):
		print(list(capitals.values()))
			
	elif(num == 4):
		name = input("What is the country's name?")
		print(capitals.get(name,"Not found"))

	elif(num == 5):
		d = input("What Country do you want to delete.")
		del(capitals[d])

	else:
		break

