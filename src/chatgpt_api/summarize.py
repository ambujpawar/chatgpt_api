import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")

completion = openai.ChatCompletion(
    engine="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "What is the circumference in km of the planet Earth?"}]
)

print(completion)

reply_content = completion.choices[0].message.content
print(reply_content)

