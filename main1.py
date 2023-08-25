from cv2 import cv2
import pytesseract
import pandas as pd
import numpy as np
import math
from matplotlib import pyplot as plt


img = cv2.imread('images/image-7.jpg',0)img_copy = img.copy()
img_canny = cv2.Canny(img_copy, 50, 100, apertureSize = 3)