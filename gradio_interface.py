import gradio as gr
from module import preprocess, detection

def imei_from_image_(inp):
    gray_scale = preprocess.gray_scale(inp)
    result = detection.find_imei(gray_scale)

    return result

demo = gr.Interface(fn=imei_from_image_, inputs="image", outputs="text")
demo.launch()