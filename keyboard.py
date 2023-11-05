from pynput.keyboard    import Controller as keyboard
from pynput.keyboard    import Listener, Key

board   = keyboard()

def enter():    tap(Key.enter)
def tab():      tap(Key.tab)
def right():    tap(Key.right)
def down():     tap(Key.down)
def shift():    tap(Key.shift)

def press(a):   board.press(a)
def release(a): board.release(a)
def tap(a):     board.press(a), board.release(a)
def hotkey(*args):  [press(b) for b in args]; [release(b) for b in args]

def write(a):       [tap(b) for b in a]
def command(*args): [(write(b), enter())    for b in args]

def listen():
    def on_press(key):  return key is not Key.esc
    with Listener(on_press=on_press) as listener: listener.join()