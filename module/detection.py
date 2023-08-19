from typing import List
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
        for k in res:
            if ord(k) > 47 and ord(k) < 58: # remove 
               res_filter = res_filter + k
        if res.find("IMEI") != True:
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
    
    # for token in ocr_str:
    #     if token[0] == "I":
    #         if token[0] == "I" and token[1] == "M" and token[2] == "E" and token[1] == "I" 
            
    text = pytesseract.image_to_string(image, config="--psm 11 --oem 1")
    
    line_flag = False
    tokens = text.split("\n")
    result = []
    for i,token in enumerate(tokens):
        var = token.find("IMEI")
        if var == 0:
            imei_token = token.replace(" ", "")
            line_flag = True
            if len(imei_token) > 18:
                #imei_number = imei_token.split(":")
                result.append(imei_token)
                line_flag = False
            else:
                while line_flag:
                    j = i + 1
                    if len(tokens[j]) > 14:
                        for k in tokens[j]:
                            if ord(k) < 48 and ord(k) > 57:
                                line_flag = False
                                break
                        if line_flag:        
                            result.append(tokens[j])
                            line_flag = False 
                    else:
                        i=i+1
    if len(result)>0:
        return make_response(result)
    return "No IMEI NUMBER DETECTED!"



               