from karel.stanfordkarel import *

# Here is a place to program your Section problem

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move_to_beeper()
    # build hospital 
    build_hospital()
    move()
    move()
    move()
    move()
    move()
    build_hospital()
    move()

def build_hospital():
    turn_left()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

        
def move_to_beeper():
    # Move until Karel finds a beeper
    move()
    move()

if __name__ == '__main__':
    main()