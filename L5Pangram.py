pangram=""
n = input("Enter a number")
numbers={"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
for c in n:
	if c in numbers:
		numbers[c]+=1

for c in numbers.values():
	if c == 0:
		pangram = False
		break
	else:
		pangram = True

if pangram == False:
	print("This is not a pangram")
else:
	print("This is a pangram")
		
	