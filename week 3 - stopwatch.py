# template for "Stopwatch: The Game"

import simplegui

# define global variables
time = 0
wins = 0
tries = 0
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenths = t % 10
    total_seconds = (t - tenths) / 10
    disp_seconds = total_seconds % 60
    minutes = (total_seconds - disp_seconds) / 60
    
    if disp_seconds < 10:
        disp_seconds = "0" + str(disp_seconds)
    else:
        disp_seconds = str(disp_seconds)
    
    return str(minutes) + ":" + disp_seconds + "." + str(tenths)
    

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    global running
    timer.start()
    running = True
    
    
def stop_timer():
    global time, tries, wins, running
    timer.stop()
    if running == True:
        running = False
        tries += 1
        if time % 10 == 0:
            wins += 1
    
def reset_timer():
    global time, tries, wins
    time = 0
    tries = 0
    wins = 0
    timer.stop()


# define event handler for timer with 0.1 sec interval
def increment_time():
    global time
    time += 1


# define draw handler
def display_time(canvas):
    canvas.draw_text(format(time), (130, 130), 150, 'green', 'monospace')
    score = str(wins) + "/" + str(tries)
    canvas.draw_text(score, (725, 25), 25, 'white', 'monospace')
    
    
# create frame
f = simplegui.create_frame("Stopwatch: The Game!", 800, 175)


# register event handlers
timer = simplegui.create_timer(100, increment_time)
f.add_button("Start", start_timer, 60)
f.add_button("Stop", stop_timer, 60)
f.add_button("Reset", reset_timer, 60)


# start frame
f.start()
f.set_draw_handler(display_time)


# Please remember to review the grading rubric
