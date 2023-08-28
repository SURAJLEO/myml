import gradio as gr
import random
import time

# Define a custom CSS style to add icons
custom_css = """
<style>
    .gradio-text-box::placeholder {
        color: #888;
    }
    .gradio-text-box.user::before {
        content: '👤';
        margin-right: 8px;
    }
    .gradio-text-box.bot::before {
        content: '🤖';
        margin-right: 8px;
    }
</style>
"""

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(style=custom_css)
    clear = gr.Button("Clear")

    def user(user_message, history):
        return "", history + [[user_message, None, 'user']]

    def bot(history):
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        history[-1][1] = ""
        for character in bot_message:
            history[-1][1] += character
            time.sleep(0.05)
            yield history, 'bot'

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)
    
demo.queue()
demo.launch()
