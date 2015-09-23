# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui, random, math

game_range = 100


# helper functions
def new_game():
    """
    Starts a new game.
    """
    global secret_number, game_range, guesses_left
    secret_number = random.randrange(0, game_range)
    guesses_left = int(math.ceil(math.log(game_range + 1)/math.log(2)))
    print ""
    print "New game with range [0, " + str(game_range) + ")"
    print "Guesses left: " + str(guesses_left)
    
def use_guess():
    """
    Counts the number of guesses a player has left and starts
    a new game when they run out.
    """
    global guesses_left
    guesses_left -= 1
    if guesses_left > 0:
        print "Guesses left: " + str(guesses_left)
    else:
        print "Sorry, no guesses left :("
        new_game()
        


# define event handlers for control panel
def range100():
    """
    Starts a new game with range [0, 100).
    """
    global game_range
    game_range = 100
    new_game()

def range1000():
    """
    Starts a new game with range [0, 1000).
    """
    global game_range
    game_range = 1000
    new_game()
    
def input_guess(guess):
    """
    Compares a player's guess to the computer's number.
    """
    print ""
    print "Guess was " + guess
    guess = int(guess)
    if guess < secret_number:
        print "Higher!"
        use_guess()
    elif guess > secret_number:
        print "Lower!"
        use_guess()
    else:
        print "Correct!"
        new_game()
        

# create frame
frame = simplegui.create_frame("Guess the number!", 0, 300, 200)


# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Put in a number & hit enter:", input_guess, 200)


# call new_game 
new_game()