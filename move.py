#https://github.com/erlaarnalds/hrverkefni

TEN=10
ONE=1

def position(k_int):
    '''creates the x-axis and puts the creature in position k_int'''
    x_axis_str='xxxxxxxxxx'

    x_axis_left=x_axis_str[:(k_int-1)]
    x_axis_right=x_axis_str[k_int:]

    creature_position_str = x_axis_left + 'o' + x_axis_right
    return creature_position_str

def move(n_str, i_int):
    '''uses the function position to move the creature to 
    the preferred direction. If the creature is at one end it
    will stop there.'''
    
    new_position=''

    if n_str=='l':
        if i_int!=ONE:
            i_int=i_int-1

    else: #if n_str is 'r'
        if i_int!=TEN:
            i_int=i_int+1
        
    new_position = position(i_int)
    return new_position, i_int


n_int=int(input('Input a position between 1 and 10: '))
print(position(n_int))

print('l - for moving left')
print('r - for moving right')
print('Any other letter for quitting')

direction=input('Input your choice: ')

while direction=='r' or direction=='l':
    new_position, n_int= move(direction, n_int)
    print(new_position)

    direction=input('Input your choice: ')

print(new_position)


