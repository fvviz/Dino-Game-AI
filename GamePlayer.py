import numpy as np
from skimage.io import imread
import os
import matplotlib.pyplot as plt
from tqdm import tqdm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import confusion_matrix as confmat
from PIL import ImageGrab
import time
from pynput.keyboard import Controller , Key


np.set_printoptions(threshold=np.inf)

keyboard = Controller()

negExamples = os.path.join(r"C:\Users\home\Desktop\Artifcial intelligence\ML\data\dinodata\neg examples")
posExamples = os.path.join(r"C:\Users\home\Desktop\Artifcial intelligence\ML\data\dinodata\pos examples")


negarray = np.zeros((109,92075))

n = 0

for neg in tqdm(os.listdir(negExamples)):
    file = imread(f"C:/Users/home/Desktop/Artifcial intelligence/ML/data/dinodata/neg examples/{neg}",as_gray=True).flatten()
    negarray[n,:] = file
    n +=1

posarray = np.zeros((117,92075))

m = 0

for pos in tqdm(os.listdir(negExamples)):
    file = imread(f"C:/Users/home/Desktop/Artifcial intelligence/ML/data/dinodata/pos examples/{pos}",as_gray=True).flatten()
    posarray[m,:] = file
    m +=1


posclasses = np.ones((117,1))
negclasses = np.zeros((109,1))
classes = np.concatenate([posclasses,negclasses], axis=0)


data  = np.concatenate([posarray,negarray],axis = 0)


clf = LogisticRegression()
clf.fit(data,classes)

def Start():
    time.sleep(2)

    while True:
        cap = ImageGrab.grab(bbox=(485,139,1120,284))
        capsave = cap.save(f"caps/pic.png")
        array = imread(f"caps/pic.png",as_gray = True).flatten()

        pred = clf.predict([array])

        if pred == [1.]:
            keyboard.press(Key.up)
            keyboard.release(Key.up)
            print("jumping")

        time.sleep(0.08)

Start()
