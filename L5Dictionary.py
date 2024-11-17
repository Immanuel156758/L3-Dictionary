v = input("Enter a word")
vowels = {"a": 0, "e": 0, "o": 0, "i": 0, "u": 0}
for c in v:
	print(c)
	if c in vowels:
		vowels[c]+=1
print(vowels)

