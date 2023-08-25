import cv2 
from typing import List
import sys
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
def image_validation(path : str) -> bool:
    """
    Method to determine whether right path given or not.

    Parameters
    ----------
    path
        Path of image
    
    Return 
    ------
    bool
    """
    token = path.split('.')
    img_extension = ['jpg', 'jpeg', 'png']
    if token[-1] in img_extension:
        return True
    return False
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
        if image_validation(inp_image):
            image = read_image(inp_image)
            resize_image = preprocess.resize(image)
            # cv2.imshow("Image", image)
            gray_scale = preprocess.gray_scale(resize_image)
            result = detection.find_imei(gray_scale)
            print("Result", result)
            option = input(
                           """\n Want to use again, Press 'y'. 
                                 Otherwise, Press 'n'. \n
                                 
                            """)
            if option == 'n' or option == "N":
                flag = False
                print("""
                Good Bye have a nice day!
                See you soon!
                """)
            elif option == 'Y' or option == "y":
                print("""
                    Welcome Again!
                    """)
        else:
            print("Wrong File Format. Provide right  address") 



if __name__ == "__main__":
    main()