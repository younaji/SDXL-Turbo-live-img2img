import gradio as gr

markdown_text_img = """
# [Stable Diffusion을 이용한 나만의 아바타 생성기]
#### Stable Diffusion 기술을 기반으로 원하는 이미지 스타일을 선택하고 프롬프트를 작성하여 나만의 아바타 캐릭터를 생성해보세요!
"""
markdown_text_video = """
# [Stable Video Diffusion을 이용한 릴스 생성기]
#### Stable Video Diffusion 기술을 이용하여 생성한 캐릭터를 움직이는 릴스로 만들어보세요!
"""

def gen(thema, positive_text, negative_text, slider1, slider2, input_image):
    return thema, positive_text, negative_text, slider1, slider2, input_image


with gr.Blocks() as demo:
    with gr.Tab("Image generator") :
        gr.Markdown(markdown_text_img)
        with gr.Row():
            with gr.Column():
        
                gr.Dropdown(["SDXL Turbo"], label= "model")
                with gr.Tab("Prompting") : 
                    thema=gr.Radio(["Avatar", "Marvel", "Ghibli", "Thema1", "Thema2"], label="Thema")

                    positive_text = gr.Text(label="Prompt", placeholder="원하는 이미지에 대한 프롬프트를 작성하세요")
                    negative_text = gr.Text(label="Negative Prompt", placeholder="이미지에 포함하지 않을 프롬프트를 작성하세요")

                with gr.Tab("Fine-tuning") :    
                    slider1 = gr.Slider(minimum=1, maximum=150, label="Sampling steps")
                    slider2 = gr.Slider(minimum=1, maximum=30, label="CFG Scale")

     
            input_image = gr.Image(label="My Image")

    
        gen_btn = gr.Button("Generate")

        output_image = gr.Image(label="Output Image")
   
        gen_btn.click(fn=gen, inputs=[thema, positive_text, negative_text, slider1, slider2, input_image], outputs=output_image)



    with gr.Tab("Video generator") :
        gr.Markdown(markdown_text_video)


demo.launch(server_port=7889, debug=True, share=True)