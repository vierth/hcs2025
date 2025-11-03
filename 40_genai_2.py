import ollama 

messages = [
    {'role':'system', 'content':"""
     You are an expert in Ming dynasty history. You have knowledge of the fall of the dynasty etc etc.
     """},
    {'role':'user','content':'Who was Wei Zhongxian?'},
    {'role':'user', "content": 'Who was the Tianqi Emperor?'},
    {'role':'user', "content":"When was the Ming dynasty?"}
]

with open('output.txt','w',encoding='utf8') as wf:
    for part in ollama.chat(
        model='gpt-oss',
        messages=messages,
        options={
            'temperature':1.0 # set this from 0 to 1
        },
        stream=True
    ):
        wf.write(part['message']['content'])
        print(part['message']['content'], end='', flush=True)