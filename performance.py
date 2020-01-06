import glob
# Just disables the warning, doesn't enable AVX/FMA
import os
import sys
import time
import tkinter
from tkinter import *
#import Tkconstants
#import tkFileDialog
from tkinter import filedialog
import shutil
import cv2 
from PIL import Image

image_list = []





A=glob.glob("/home/vaibhav/yolo/darknet/test_data/imaged_tryout/imaged_tryout/*.jpg")
#os.system('./darknet detector test food.data cfg/food.cfg food_backup/food_18200.weights')

#for filename in A[3:5]: #assuming gif
    #im=Image.open(filename) 
    #print(filename)
    #with Image.open(filename) as image: 
    #    width, height = image.size     
    #    rgb_im = image.convert('RGB')
    #im = cv2.imread(filename)
    #cv2.imshow("image",im)
    #cv2.waitKey(1000)
    #image_list.append(im)
    #os.system('./darknet detector test food.data cfg/food.cfg food_backup/food_18200.weights filename')


for i in range(0, 1):    #len(A)-1):
  B=A[i]
  C=B[27:]
  image=open(C)
  print(isinstance(C, str))
  #img = cv2.imread(C)
  #img=mpimg.imread(C)
  #cvShowImage('image', img)('image', img)
  #print(img)
  #os.system('./darknet detector test food.data cfg/food.cfg food_backup/food_18200.weights C')
  #os.system('B')
   


#os.system('./darknet detector test food.data cfg/food.cfg food_backup/food_18200.weights 20.jpg') 
#time.sleep(1)
#os.system('sudo python spawn_npc.py -n 10 -w 0 &')
#os.system('sudo python Simulator_Adversary.py &')
