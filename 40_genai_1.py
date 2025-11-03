import ollama 

messages = [
    {'role':'system', 'content':"""
     You are an expert in Ming dynasty history. You have knowledge of the fall of the dynasty etc etc.

     You reply only in limricks
     """},
    {'role':'user','content':'Who was Wei Zhongxian?'}
]

response = ollama.chat(
    model='gpt-oss',
    messages=messages,
    options={
        'temperature':1.0 # set this from 0 to 1
    }
)


print(response['message']['content'])