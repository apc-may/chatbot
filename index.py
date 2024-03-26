import gradio as gr

#gr.Interface.load(
#    "huggingface/google/vit-base-patch16-224",
#    examples=["./images/cat.jpg", "./images/man.jpg"]).launch()


def echo(message, history):
    return message

demo = gr.ChatInterface(fn=echo, examples=["hello", "hola", "merhaba"], title="Echo Bot")
demo.launch() 