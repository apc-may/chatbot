import gradio as gr

#gr.Interface.load(
#    "huggingface/google/vit-base-patch16-224",
#    examples=["./images/cat.jpg", "./images/man.jpg"]).launch()

#Webアプリ内で実行する関数を定義
def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet,      #Webアプリ内で実行する関数
                    inputs="text", #関数への入力値
                    outputs="text")#関数の出力値

demo.launch()  