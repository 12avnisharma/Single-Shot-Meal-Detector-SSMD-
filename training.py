import glob
import os
import tkinter
from tkinter import *
#import Tkconstants
#import tkFileDialog
from tkinter import filedialog
import shutil

'''
while True:
    print("Please select your image directory.")
    #current_dir = tkFileDialog.askdirectory()
    current_dir = filedialog.askdirectory()
    if current_dir == None or current_dir == "":
        print("You must select a directory.")
        continue
    break

print(current_dir)
'''

A=glob.glob("/home/vaibhav/yolo/darknet/try/*.jpg")
file_train = open('train.txt', 'w')
#source="/home/vaibhav/yolo/da/Imagenet/VOCdevkit/VOC2007/JPEGImages/"
#dest="/home/vaibhav/yolo/da/Imagenet/VOCdevkit/VOC2007/images/"
for i in range(0, len(A)-1):
  B=A[i]
  #C=B[56:-4]+'.JPEG'
  #s=source+C
  #d=dest+C
  #shutil.copy(s,d)
  file_train.write(B)
  file_train.write('\n')
