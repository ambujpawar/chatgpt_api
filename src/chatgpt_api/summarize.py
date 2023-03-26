import os
# Third party imports
from dotenv import load_dotenv
import gradio as gr
import openai
import tiktoken

load_dotenv()
openai.api_key = os.getenv("API_KEY")


def chatgpt_summarize(user_input: str, role: str = "user"):
    messages=[
        {"role": "user", "content": "You are a summarizer bot. I provide you with a long text and you summarize it"},
        {"role": "assistant", "content": "OK!"}
        ]
    messages.append({"role": role, "content": user_input})
    num_tokens = num_tokens_from_messages(messages)
    
    # Check if the text is too long. Limit is 4000 tokens
    # So, we have selected 3000 tokens for user and it gives 
    # 1000 tokens for the bot to reply
    if num_tokens > 3000:
        return "The text is too long. Please enter a shorter text."
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", #This is 0301 model
        messages=messages,
    )
    reply_content = completion.choices[0].message.content
    return reply_content


def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301"):
  """Returns the number of tokens used by a list of messages."""
  try:
      encoding = tiktoken.encoding_for_model(model)
  except KeyError:
      encoding = tiktoken.get_encoding("cl100k_base")
  if model == "gpt-3.5-turbo-0301":  # note: future models may deviate from this
      num_tokens = 0
      for message in messages:
          num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
          for key, value in message.items():
              num_tokens += len(encoding.encode(value))
              if key == "name":  # if there's a name, the role is omitted
                  num_tokens += -1  # role is always required and always 1 token
      num_tokens += 2  # every reply is primed with <im_start>assistant
      return num_tokens
  else:
      raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.""")


if __name__ == "__main__":
    input_text = gr.inputs.Textbox(label="Input Text")
    output_text = gr.outputs.Textbox(label="Summary")

    demo = gr.Interface(fn=chatgpt_summarize, inputs=input_text, outputs=output_text, title="Summarizer App", description="Enter a long text and get a summary using ChatGPT.").launch()
    demo.launch()
