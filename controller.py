from keyboard import command, Key, hotkey, enter, right
import time
def restart():      command('exit()','python','from controller import restart as r',
                        'from vpn import subCountry as s')
def wait(*args):    time.sleep(.1) if not args else time.sleep(args[0])
def dock(a):        hotkey(Key.cmd_l,'t'), wait(), [(right(), wait(.01)) for i in range(a-1)], enter()
def loop(a,b,c):    [(a(),wait(c)) for d in range(b)] 