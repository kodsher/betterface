from PIL import Image, ImageGrab
import cv2, random
import mse.tools
def capture(a):
        time.sleep(.1)
        start()
        here = m.position
        pos((0,0))
        time.sleep(.3)
        global b,c,d,e
        monitor = {"top": c, "left": b, "width": d-b, "height": e-c}
        sct_img = mss.mss().grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=sp+str(a)+'.png')
        pos(here)
def center(a):
     return(a.left+a.width/2,a.top+a.height/2)