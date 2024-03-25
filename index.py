import gradio as gr

gr.Interface.load(
    "huggingface/google/vit-base-patch16-224",
    examples=["./images/cat.jpg", "./images/man.jpg"]).launch()