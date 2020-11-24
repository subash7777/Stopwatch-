# template for "Stopwatch: The Game"
import simplegui
# define global variables
c = 0
message = "0:00.0"
x = 0
y = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    abc = t / 10
    d = t % 10
    a = abc / 60
    bc = abc % 60
    if len(str(bc)) == 1:
        return str(a)+':0'+str(bc)+'.'+str(d)
    elif len(str(bc)) == 2:
        return str(a)+':'+str(bc)+'.'+str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def startb():
    timer.start()
    
def stopb():
    if timer.is_running():
        timer.stop()
        global x,y
        y = y + 1
        if c % 10 == 0:
            x = x + 1
    
def resetb():
    timer.stop()
    global c, message,x,y
    c=0
    message = "0:00.0"
    x=0
    y=0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global c, message
    c = c + 1
    message = format(c)
     
# define draw handler
def draw(canvas):
    canvas.draw_text(message, [100,100], 36, "Red")
    canvas.draw_text(str(x)+'/'+str(y), [240,30], 36, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)
# register event handlers
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)
frame.add_button("Start", startb, 100)
frame.add_button("Stop", stopb, 100)
frame.add_button("Reset", resetb, 100)
# start frame
frame.start()
