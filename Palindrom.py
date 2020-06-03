def palindrom(string):
	a = ''
	for i in range(len(string)):
		a += string[len(string)-1-i]
	return a

string = input("Enter a word: ")
a = palindrom(string)
if a == string:
	print("This is a palindrome.")
else:
	print("This is not a palindrome.")