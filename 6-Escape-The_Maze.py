def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def right_move():
    turn_right()
    move()

def movement():
    if wall_in_front() and right_is_clear():
        right_move()
    elif wall_in_front():
        turn_left()
    elif front_is_clear() and not right_is_clear():
        move()
    elif front_is_clear() and right_is_clear():
        right_move()
    elif right_is_clear():
        turn_right()

while front_is_clear():
    move()

turn_left()

while not at_goal():
    movement()