from typing import List
import cv2
import re
from pyzbar.pyzbar import decode
import pytesseract


# def validate_imei(var_str: str) -> bool:
#     count = -1
#     for i in range(15):
#         if ord(var_str[-(i)]) > 47 and ord(var_str[-(58)]) < 58:
#             count = count + 1
#     if count == 14:
#         return True
        
def make_response(result_list: List[str]) -> List[str]:
    """
    Clean the response 

    Parameters
    ----------
    result_list:
        list of detected response
    
    Return
    ------
    List[str] 
    """
    result = list(set(result_list))
    for i, res in enumerate(result):
        res_filter =""
        # for k in res:
        #     if ord(k) > 47 and ord(k) < 58: # remove 
        #        res_filter = res_filter + k
        if re.search("IME*",res):
        #if res.find("IME*") != True:
            result[i] = "IMEI: "+res_filter
    return result

def find_imei(image) -> List[str]:
    """
    Find IMEI from string.

    Parameters
    ----------
    image
        Image t find imei.

    Return
    ------
    List[str]
    """
    text = pytesseract.image_to_string(image, config="--psm 12 --oem 1")
    # Decode the barcode image
    result = []
    detectedBarcodes = decode(image)
    # If not detected then print the message
    if detectedBarcodes:
        print('detectedBarcodes\n')
        # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:
            # # Locate the barcode position in image
            # (x, y, w, h) = barcode.rect	
            # # Put the rectangle in image using
            # # cv2 to highlight the barcode
            # cv2.rectangle(img, (x-10, y-10),
            #             (x + w+10, y + h+10),
            #             (255, 0, 0), 2)	
            if barcode.data!="":
        # Print the barcode data
                if len(barcode.data) <17:
                    print("InLength")
                    result.append("Barcode Data : " + str(barcode.data))
    else:
        tokens = text.split("\n")
        tokens.remove("")
        print(tokens)
        for i, token in enumerate(tokens):
            print(f"Token: {token}")
            var = token.find("IMEI")
            if var == 0:
                print("Var", var)
                imei_token = token.replace(" ", "")
                print("imei_token", imei_token)
                line_flag = True
                if len(imei_token) > 18:
                    #imei_number = imei_token.split(":")
                    result.append(imei_token)
                    line_flag = False
                else:
                    while line_flag:
                        j = i + 1

                        if len(tokens[j]) > 14 :
                            for k in tokens[j]:
                                if ord(k) < 48 and ord(k) > 57:
                                    line_flag = False
                                    break
                            if line_flag:        
                                result.append(tokens[j])
                                line_flag = False 
                        else:
                            i=i+1
    if len(result) > 0:
        #response = make_response(result)
        #print("response", response)
        return result
    return "No IMEI NUMBER DETECTED!"



               