""" Preprocess the image input by user"""
import cv2
import PIL
from PIL import Image
from typing import List

def resize(image) -> List[List[float]]:
    """
    Resize the given image in 256x256.

    Parameters
    ----------
    image
        Image for resizing.
    
    Return 
    ------
    Image list[list[float]]
    """
    resize_image = cv2.resize(image, (256,256), interpolation = cv2.INTER_AREA) #interpolation helps to maintain aspect ratio
    return resize_image

def gray_scale(image) -> List[List[float]]:
    """
    Reduce number of channels.

    Parameters
    ----------
    image
        Image for grayscale.
    
    Return 
    ------
    Image list[list[float]]
    """
    try:
        if image.ndim == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            return gray
        return image
    except Exception:
        print(Exception)

     
        



