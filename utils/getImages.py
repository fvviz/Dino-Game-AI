from PIL import ImageGrab
from pynput.keyboard import Controller , Listener , Key
import win10toast

capture_box = (485, 139, 1120, 284) # capture  a 635x135 image
bruh = (644,308,1279,443)

jump_key = Key.space # whenever this key is pressed, Capture a positive example
ignore_key = Key.caps_lock # whenever this key is pressed, Capture a negative example

pos_start_val = 188
neg_start_val = 327




pos_img_path = "../data/pos examples"
neg_img_path = "../data/neg examples"

notifier = win10toast.ToastNotifier()

print(f"""
Dino Game Ai by fwiz
--------------------

Image Capturer launched successfully

--------------------
Current Configs

Jump key : {jump_key}
Ignore key : {ignore_key}

Positive Example Starting value : {pos_start_val}
Negative Example Starting value : {neg_start_val}

Positive Example Save folder : {pos_img_path}
Negative Example Save folder : {neg_img_path}

-------------------------------------------------

""")

def capture_image(capture_box,start_val,path):
    capture = ImageGrab.grab(bbox=capture_box)
    capture.save(f"{path}/example{start_val}.png")


def on_press(key):
    global pos_start_val
    global neg_start_val
    if key == jump_key:
        capture_image(bruh,pos_start_val,pos_img_path)
        pos_start_val = pos_start_val + 1

        print(f"({pos_start_val}) jumped")
    elif key == ignore_key:
        capture_image(bruh,neg_start_val,neg_img_path)
        neg_start_val = neg_start_val + 1

        print(f"({neg_start_val}) ignored")
def on_release(key):
    pass

listener = Listener(on_press=on_press,on_release=on_release)
with listener as listener:
    listener.join()

