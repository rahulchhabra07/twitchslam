#!/usr/bin/env python3

import cv2 
import numpy as np
import sdl2
import sdl2.ext

from display import Display


W, H = 540, 270

display = Display (W, H)

def process_frame(img):
  display.paint(img)
  print (img.shape)


if __name__ == "__main__":
  testvid = cv2.VideoCapture('test.mp4')
  while testvid.isOpened():
    ret, frame = testvid.read()  
    if ret:
      process_frame(frame)
    else:
      break

