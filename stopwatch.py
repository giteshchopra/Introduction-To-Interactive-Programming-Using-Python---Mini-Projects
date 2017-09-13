#combining text drawing in the canvas with timers to build a simple digital stopwatch that keeps track of the time in tenths of a second. The stopwatch should contain "Start", "Stop" and "Reset" buttons.
import simplegui
# define global variables
t=0
time=''
next = 0
counter = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time
    time=str(t//600)+':'+str((t%600)//100)+str((t%100)//10)+':'+str(t%10)
   
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
def stop():
    global counter,next
    if not timer.is_running():
        return
    timer.stop()
    counter+=1
    if t%10 == 0:
        next+=1
def reset():
    global t,next,counter
    t=0
    next=0
    counter=0


# define event handler for timer with 0.1 sec interval
def count():
    global t
    t+=1


# define draw handler
def draw(canvas):
    format(t)
    canvas.draw_text(time, (100, 200), 96, "White")
    canvas.draw_text(str(next)+'/'+str(counter), (400, 50), 26, "White")
    
# create frame
frame=simplegui.create_frame("Stop Watch", 500, 500,100)


# register event handlers
frame.set_draw_handler(draw)
frame.add_button('Start',start,100)
frame.add_button('Stop',stop,100)
frame.add_button('Reset',reset,100)


timer=simplegui.create_timer(100, count)
# start frame
frame.start()
#timer.start()


