import gradio as gr
from module import preprocess, detection

def imei_from_image_(inp):
    resize_image = preprocess.resize(inp)

    gray_scale = preprocess.gray_scale(resize_image)
    result = detection.find_imei(gray_scale)
    response = {}
    
    for i,res in enumerate(result):
       response["IMEI" + str(i + 1)] = res
    return response

demo = gr.Interface(fn=imei_from_image_, inputs="image", outputs="json", examples = ["images/image-4.jpeg"], title = "IMEI Detector")
demo.launch(server_name="0.0.0.0", server_port = 7860)