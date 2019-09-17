# player byrjar í (1,1)
# Skrifa fall sem breytir string input í átt
# if setningar passa upp á að segja hverjar áttirnar eru

def travel(string, k, p):
    if string=='n':
        p=p+1
    elif string=='s':
        p=p-1
    elif string=='e':
        k=k+1
    elif string=='w':
        k=k-1
    
    return k,p

x=1
y=1

while (x!=3 or y!=3):
    if x==1:
        if y==1:
            print('You can travel: (N)orth')
            string=input('Direction: ')
            while string.lower()!='n':
                print('Not a valid direction!')
                string=input('Direction: ')
        elif y==2:
            print('You can travel: (N)orth or (E)ast or (S)outh')
            string=input('Direction: ')
            while string.lower()=='w':
                print('Not a valid direction!')
                string=input('Direction: ')
        elif y==3:
            print('You can travel: (E)ast or (S)outh')
            string=input('Direction: ')
            while string.lower()=='w' or string.lower()=='n':
                print('Not a valid direction!')
                string=input('Direction: ')
    elif x==2:
        if y==1:
            print('You can travel: (N)orth')
            string=input('Direction: ')
            while string.lower()!='n':
                print('Not a valid direction!')
                string=input('Direction: ')
        elif y==2:
            print('You can travel: (W))est or (S)outh')
            string=input('Direction: ')
            while string.lower()!='w' or string.lower()!='s':
                print('Not a valid direction!')
                string=input('Direction: ')
        elif y==3:
            print('You can travel: (E)ast or (W)est')
            string=input('Direction: ')
            while (string.lower()) != 'w' or (string.lower()) != 'e':
                print('Not a valid direction!')
                string=input('Direction: ')
    
    elif x==3:
        if y==1:
            print('You can travel: (N)orth')
            string=input('Direction: ')
            while string.lower()!='n':
                print('Not a valid direction!')
                string=input('Direction: ')
        elif y==2:
            print('You can travel: (N)orth or (S)outh')
            string=input('Direction: ')
            while string.lower()!='n' or string.lower()!='s':
                print('Not a valid direction!')
                string=input('Direction: ')

    x,y=travel(string.lower(), x, y)


print('Victory!')