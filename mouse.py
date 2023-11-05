from pynput.mouse import Controller as makeMouse
from pynput.mouse import Button
# Creates mouse object
mouse = makeMouse()

def click():    mouse.click(Button.left,1)
def to(x,y):    mouse.position = x,y
def where():    return mouse.position

