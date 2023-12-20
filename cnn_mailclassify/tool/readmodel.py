import gensim
# 加载预训练的Word2Vec模型
model = gensim.models.Word2Vec.load("trained_word2vec.model")
# 查看词汇表中的词语
print(model.wv.vocab)
# 查看某个词语的词向量
print(model.wv["text"])
# 查看两个词语的相似度
print(model.wv.similarity("text", "CNN"))
