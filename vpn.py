from keyboard import board,tab,down,enter
from mouse import mouse,where,to,click
from controller import loop,dock,wait

def subCountry(a):
    dock(1); wait()
    anchor = (993,346)
    to(anchor[0],anchor[1]), click(), wait()
    loop(tab,3,.01),loop(down,a,.01)
    enter()