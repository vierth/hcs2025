import os

def open_file(path):
    with open(path,'r',encoding='utf8') as rf:
        return rf.read()
    
def open_corpus(directory):
    texts, file_names = [], []

    for root, _, files in os.walk(directory):
        for file in files:
            if file[0] == ".":
                continue
            texts.append(open_file(os.path.join(root,file)))
            file_names.append(file)
            
    return texts, file_names

if __name__ == "__main__":
    texts, f_names = open_corpus("corpus")
    print(len(texts), len(f_names))
    
                