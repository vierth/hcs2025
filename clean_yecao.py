import re

with open('corpus/yecao.txt', 'r', encoding='utf8') as rf:
    text = rf.read()

text = re.sub(r'\n{2,}', '~~~', text)
text = re.sub(r'\n', '', text)
text = re.sub(r'~{3}', '\n\n', text)
print(text)