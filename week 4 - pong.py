# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_vel = 0
paddle2_vel = 0



# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    if direction == RIGHT:
        m = 1
    else:
        m = -1
        
    ball_vel = [m * random.randrange(120, 240) / 60, - random.randrange(60, 180) / 60]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    paddle1_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    paddle2_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    
    score1 = 0
    score2 = 0
    
    start_player = random.randrange(0, 2)
    if start_player == 0:
        spawn_ball(RIGHT)
    else:
        spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel

        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 2 - 150, 100], 100, 'red', 'monospace')
    canvas.draw_text(str(score2), [WIDTH / 2 + 100, 100], 100, 'blue', 'monospace')
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
       
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "red", "white")
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos <= 0 and paddle1_vel < 0:
        paddle1_vel = 0
    if paddle1_pos >= HEIGHT - PAD_HEIGHT and paddle1_vel > 0:
        paddle1_vel = 0
   
    if paddle2_pos <= 0 and paddle2_vel < 0:
        paddle2_vel = 0
    if paddle2_pos >= HEIGHT - PAD_HEIGHT and paddle2_vel > 0:
        paddle2_vel = 0
    
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    # draw paddles
    paddle1_end = paddle1_pos + PAD_HEIGHT
    paddle2_end = paddle2_pos + PAD_HEIGHT
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos], [HALF_PAD_WIDTH, paddle1_end], PAD_WIDTH, "white")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos], [WIDTH - HALF_PAD_WIDTH, paddle2_end], PAD_WIDTH, "white")
    
    # determine whether paddle and ball collide    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] >= paddle1_pos - BALL_RADIUS and ball_pos[1] <= paddle1_pos + PAD_HEIGHT + BALL_RADIUS:
            ball_vel[0] *= -1.1
            ball_vel[1] *= 1.1
        else:
            score2 += 1
            spawn_ball(RIGHT)
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if ball_pos[1] >= paddle2_pos - BALL_RADIUS and ball_pos[1] <= paddle2_pos + PAD_HEIGHT + BALL_RADIUS:
            ball_vel[0] *= -1.1
            ball_vel[0] *= 1.1
        else:
            score1 += 1
            spawn_ball(LEFT)
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    speed = 8
    
    if chr(key) == "W":
        paddle1_vel = - speed
    if chr(key) == "S":
        paddle1_vel = speed
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -speed
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = speed
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if chr(key) in "WS":
        paddle1_vel = 0
    
    if key in [simplegui.KEY_MAP['up'], simplegui.KEY_MAP['down']]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game)


# start frame
new_game()
frame.start()
