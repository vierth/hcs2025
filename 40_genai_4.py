import ollama
from pathlib import Path

img = Path('testimage.jpg').read_bytes()

messages = [
    {'role':'system',
     'content':"""
     You are an expert OCR system designed to detect text in Ming and Qing dynasty woodblocks.

     The blocks are read from top to bottom, right to left. There is commentary in the upper register that you should ignore. Also there might be noise on the extreme right nad left of the woodblock that you should also ignore.
     """},
     
    {'role':'user',
     'content':'Please indentify the text in this image',
     'images':[img]}
]

for part in ollama.chat(
    model='qwen3-vl',
    messages=messages,
    stream=True
):
    print(part['message']['content'], end="", flush=True)