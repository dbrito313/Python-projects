def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
            if at_goal():
                done()
        elif wall_in_front():
            turn_left()
            if wall_in_front():
                turn_right()
                if front_is_clear():
                    move()
                elif turn_left():
                    if front_is_clear():
                        move()
    elif right_is_clear():
        turn_right()
        move()
        if right_is_clear() and front_is_clear():
            turn_left()
            if wall_in_front():
                turn_around()
                if wall_in_front():
                    turn_right()
                    move()
                else:
                    turn_left()
        elif front_is_clear():
            move()
    elif front_is_clear():
        move()


   
        
        
        
    
                        
                        
                   

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
