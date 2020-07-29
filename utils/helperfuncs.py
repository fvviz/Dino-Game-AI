import numpy as np
import os
from skimage.io import imread
import random
from PIL import ImageGrab
from pynput.keyboard import Controller, Listener
import time
from tqdm import tqdm

def get_data_shape(img_path):
    files = os.listdir(img_path)

    file = random.choice(files)
    array  = imread(f"{img_path}/{file}")
    return len(files),array.shape[0]*array.shape[1]



def get_matrix_from_img(img_path):

    file_count, col_len = get_data_shape(img_path)
    data_mat =  np.zeros((file_count,col_len))

    m = 0

    for file in tqdm(os.listdir(img_path)):
        array  = imread(f"{img_path}/{file}",as_gray=True).flatten()
        data_mat[m,:] = array
        m += 1

    return data_mat




def launch_ai(model,interval,capture_box,jump_key,stop_key):

    running = True





    while running:
        screenshot = ImageGrab.grab(capture_box)
        screenshot.save("ss.png")

        array = imread("ss.png",as_gray=True).flatten()

        pred = model.predict([array])

        keyboard = Controller()


        if pred == [1]:
            keyboard.press(jump_key)
            keyboard.release(jump_key)
            print("jumping")
        else:
            pass

        time.sleep(interval)









