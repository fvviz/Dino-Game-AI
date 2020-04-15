from PIL import ImageGrab
from pynput.keyboard import Key, Listener
num = 0


def on_press(key):
    if key == Key.shift:  # take a picture when whenever shift is pressed and store it as a negative example
        global num
        print(f"shift pressed ({num})")
        cap = ImageGrab.grab(bbox=(485, 139, 1120, 284))
        nameig = f"test{num}.png"
        img= cap.save(rf"data\neg examples\test{num}.png") # save the image in the negative examples directory
        num = num + 1


    elif key == Key.caps_lock:  # take a picture when whenever capslock is pressed and store it as positive example
        global num
        print(f"shift pressed ({num})")
        cap = ImageGrab.grab(bbox=(485, 139, 1120, 284))
        nameig = f"test{num}.png"
        img = cap.save(rf"data\pos\test{num}.png") # save the image in the negative examples directory
        num = num + 1

def on_release(key):
    pass



with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
