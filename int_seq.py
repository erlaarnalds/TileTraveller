num=int(input('Enter an integer: '))
cumsum=0
maxnum=0
odd=0
even=0

while num>0:
    cumsum=cumsum+num
    print('Cumulative total: ', cumsum)
    
    #finding the maximum number
    if num>maxnum:
        maxnum=num
    
    #counting odd and even numbers
    if num%2==0:
        even+=1
    else:
        odd+=1

    num=int(input('Enter an integer: '))

#print info after integer intake has stopped
#maxnum is zero only if the while loop has not been entered,
#so we use that to control whether info is printed or not

if maxnum!=0:
    print('Largest number: ', maxnum)
    print('Count of even numbers: ', even)
    print('Count of odd numbers: ', odd)