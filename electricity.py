id1=110022
print('\t\t\tWelcome to Delhi Electricity Board\n')
id2=int(input('enter your meter id:'))
if id1 == id2:
    print('id verified.\n')
else :
    print("invalid")
units=int(input('total no. of units consumed:'))
amount=units*20
print('Your Electricity Bill =',amount)