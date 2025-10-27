import gensim
import gensim.downloader

print(list(gensim.downloader.info()['models'].keys()))

vectors = gensim.downloader.load('word2vec-google-news-300')

print(vectors['government'])

print(vectors.most_similar('government', topn=25))

print(vectors.most_similar(positive=['king', 'woman'], negative=['man']))