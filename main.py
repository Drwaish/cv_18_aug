import cv2 
from typing import List

from module import preprocess, detection

#image = cv2.imread('images/image-1.png')
def input_path() -> str:
    """
    Get path of image to read image
    
    Parameters
    ----------
    None

    Return
    ------
    str
    """
    img_path = input("Enter path of image : ")
    return img_path

def read_image(image_path : str) -> List[List[float]]:
    """
    Load the image from given path

    Parameters
    ----------
    image_path
        Path of image to read

    Return
    ------
    Image
    """
    img = cv2.imread(image_path)
    return img

def main() -> None:
    """
    Main of code to perform operation
    
    Parameters
    ----------
    None

    Return
    ------
    None
    """
    flag = True
    while flag: 
        inp_image = input_path()
        image = read_image(inp_image)
        #resize_image = preprocess.resize(image)
        #cv2.imshow("Image", resize_image)
        gray_scale = preprocess.gray_scale(image)
        result = detection.find_imei(gray_scale)
        print("Result", result)
        option = input("""\n        Want to use again Press 'y'. 
                         Otherwise press 'n'. """)
        if option == 'n' or option == "N":
            flag = False
            print("""
            Good Bye have a nice day!
            See you soon
            """)
        elif option == 'Y' or option == "y":
            print("""
                Welcome Again!
                """)



if __name__ == "__main__":
    main()