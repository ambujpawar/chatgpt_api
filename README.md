# Summarize your articles using CHATGPT
Code to interact with ChatGPT API. The aim was to gain first hand experience working with the new chat completion API provided by API and also learning Gradio.


## Prerequisites
You need to get your own OpenAI api key. You can find it over [here](https://platform.openai.com/account/api-keys)
Simply create a new API key and write in .env file in the root of the repo in the following format:

```
API_KEY=YOUR_KEY_HERE
```

## Installation
The installation is managed by poetry. You can simply install them by:

```bash
pip install poetry
poetry env use python3.10
poetry shell
poetry install
```

## RUN
The application can be run using the following command:
```python
python summarize.py
```

## DEMO
A simple demo of the summarizer can be found here:


https://user-images.githubusercontent.com/19887541/227788251-a45929f8-9589-4b43-b743-5ebe8ae3857f.mov



