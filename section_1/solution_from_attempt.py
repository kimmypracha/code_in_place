from karel.stanfordkarel import *

def main():
    while front_is_clear():
        move_to_beeper()
        build_hospital()
        safe_move()

def safe_move():
    if front_is_clear():
        move()

def move_to_beeper():
    while no_beepers_present():
        safe_move()

def build_upward():
    turn_left()
    for i in range(2):
        move()
        put_beeper()
    turn_right()

def build_downward():
    put_beeper()
    turn_right()
    for i in range(2):
        move()
        put_beeper()
    turn_left()

def build_hospital():
    build_upward() 
    move()
    build_downward()

def turn_right():
    for i in range(3):
        turn_left()
        
if __name__ == "__main__":
    main()