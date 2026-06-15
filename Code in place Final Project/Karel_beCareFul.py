'''Karel_SurviveGame'''
from stanfordkarel import *

def main():
    '''main function'''
    # Greeting
    print('Welcome! Now this is your task you have to collect all the beepers')
    print("That's it. Goodluck!")
    print('(w : move north , a : move west , s : move south , d : move east)')

    # var beepers to collect
    count_beepers = 0

    # var beepers on the floor
    floor_beepers = 1

    # Loop
    while True:
        if beepers_present():
            pick_beeper()
            count_beepers += 1
            floor_beepers -= 1
            print(f'Need {floor_beepers} more beeper!')

        if count_beepers == 1:
            break
        print()

        # input move
        m = input('Which direction? : ').lower()

        # move forward
        if m == 'w':
            forward()

        # move left
        elif m == 'a':
            left()

        # move right
        elif m == 'd':
            right()

        # move back
        elif m == 's':
            down()
    
    # End
    print('-'*50)
    print('You are now collected all the beepers!!')
    print('Thank you for playing this game!')
    print('Wish you have a wonderful day. Bye!!')



def forward():
    '''move forward'''
    if facing_north() and front_is_clear():
        move()
    elif facing_north() and front_is_blocked():
        print("Can't go there w")
    else:
        while not_facing_north():
            turn_left()
        if front_is_clear():
            move()
        else:
            print("Can't go there wd")

def left():
    '''move to the left'''
    if facing_west() and front_is_clear():
        move()
    elif facing_west() and front_is_blocked():
        print("Can't go there l")
    else:
        while not_facing_west():
            turn_left()
        if front_is_clear():
            move()
        else:
            print("Can't go there ld")

def right():
    '''move to the right'''
    if facing_east() and front_is_clear():
        move()
    elif facing_east() and front_is_blocked():
        print("Can't go there r")
    else:
        while not_facing_east():
            turn_left()
        if front_is_clear():
            move()
        else:
            print("Can't go there rd")

def down():
    '''move to the right'''
    if facing_south() and front_is_clear():
        move()
    elif facing_south() and front_is_blocked():
        print("Can't go there b")
    else:
        while not_facing_south():
            turn_left()
        if front_is_clear():
            move()
        else:
            print("Can't go there bd")



if __name__ == '__main__':
    run_karel_program('karel_world')
