#libraries
from random import randint
#Code

l=['Rock(0)','Paper(1)','Scissors(2)']
print("...Rock...")
print("...Paper...")
print("...Scissors...")
print(l)

status='y'
while(status=='y'):
	comp = randint(0,2) #generate random int
	###
	print("Choose Rock-Paper-Scissors")
	user=int(input())
	print('---------------------')
	print("You:"+l[user])
	print("Computer:"+l[comp])
	print('---------------------')
	print('')
	print('*********************')
	if(user==comp):
		print('TIE GAME')
	elif(user==0):
		if(comp==2):
			print('Winner Winner Chicken Dinner')
		else:
			print('Sore Loser')
	elif(user==1):
		if(comp==0):
			print('Winner Winner Chicken Dinner')
		else:
			print('Sore Loser')
	elif(user==2):
		if(comp==1):
			print('Winner Winner Chicken Dinner')
		else:
			print('Sore Loser')
	print('*********************')
	print('')
	print('Play Again ? Yes-y No-n')
	status=input()
