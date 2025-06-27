import numpy as np
print('\t\t\t\tHousehold Expenses')
bills=np.array([[1,1500],[2,8000],[3,10000]])
bill=int(input())
if bill==1:
    print('Water Bill')
elif bill==2:
    print('Electricity Bill')
else:
    print('groceries')
print('total bills are: ',(bills[:,1]))
print('sum ',np.sum(bills[:,1]))
print('average',np.mean(bills[:,1]))
print('highest spending category is,electricity bill: ',np.max(bills[:,1]))