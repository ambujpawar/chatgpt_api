import os
# Third party imports
from dotenv import load_dotenv
import gradio as gr
import openai

load_dotenv()
openai.api_key = os.getenv("API_KEY")


def chatgpt_summarize(user_input: str, role: str = "user"):
    messages=[
        {"role": "user", "content": "You are a summarizer bot. I provide you with a long text and you summarize it"},
        {"role": "assistant", "content": "OK!"}
        ]
    messages.append({"role": role, "content": user_input})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", #This is 0301 model
        messages=messages,
    )
    reply_content = completion.choices[0].message.content
    return reply_content


def summarize_text(text):
    summary = chatgpt_summarize(text, role="user")
    return summary


if __name__ == "__main__":
    input_text = gr.inputs.Textbox(label="Input Text")
    output_text = gr.outputs.Textbox(label="Summary")

    demo = gr.Interface(fn=summarize_text, inputs=input_text, outputs=output_text, title="Summarizer App", description="Enter a long text and get a summary.").launch()
    demo.launch()
