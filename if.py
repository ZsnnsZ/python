number = 23
guess = int(input('Enter an integer: '))
if guess == number:
	print ('yes')
elif guess < number:
	print ('<')
else:
	print ('>')
print("done")
