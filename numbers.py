#https://github.com/erlaarnalds/hrverkefni
#part one:
#    1. Create range with all positive two-digit numbers
#    2. Use modulus and floor division to isolate each digit of 
#       number
#    3. See if squared digit sum is equal to org. number
#    4. If so, print number

digit_sum_squared=0
digit_sum=0

for i in range(10,100):
    digit_sum=(i//10)+(i%10)
    digit_sum_squared=digit_sum**2

    if digit_sum_squared==i:
        print(i)

#part two:
#   1. look at range of numbers 1-99
#   2. for number n, check all numbers <n if they are a divisor for n
#   3. Keep counter that updates for every divisor
#   4. If counter is exactly 10, print n   

divisor_counter=0

for i in range(1,100):
    divisor_counter=0
    for k in range(1,i+1):
        if i%k==0:
            divisor_counter+=1
        
    if divisor_counter==10:
        print(i)
