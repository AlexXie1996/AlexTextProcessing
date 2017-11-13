#-*- coding:utf-8 -*-
import os
import numpy as np
import gensim
import jieba
from collections import Counter

class MyModel(object):
	"""
	"""
	def __init__(self, model_path, words_path):
		"""
		"""
		self.model = gensim.models.word2vec.Word2Vec.load(model_path)
		self.asp = load_asp(words_path)

	def predict_proba(self, oword, iword):
		"""
		"""
		iword_vec = self.model[iword]
		oword = self.model.wv.vocab[oword]
		oword_l = self.model.syn1[oword.point].T
		dot = np.dot(iword_vec, oword_l)
		lprob = -sum(np.logaddexp(0, -dot) + oword.code*dot)
		return lprob

	def relative_words(self, word):
		"""
		"""
		r = {i:self.predict_proba(i, word)-0.9*np.log(j.count) for i,j in 				self.model.wv.vocab.items()}
		return Counter(r).most_common()

	def keywords(self, s):
		"""
		"""
		s = jieba.cut(s)
		s = [w for w in s if w in self.model]
		ws = {w:sum([self.predict_proba(u, w) for u in s]) for w in s}
		return Counter(ws).most_common()

	def aspect(self, s):
		"""
		"""
		asp_list = []
		s = jieba.cut(s)
		asp_list = [i for i in s if i in self.asp]

		return asp_list

def load_asp(word_path):
	"""
	"""
	ret = []
	with open(word_path, 'r',encoding='utf-8') as f:
		while True:
			word = f.readline()
			if not word:
				break
			if word is "":
				continue
			ret.append(word.strip())

	return ret

if __name__ == '__main__':

	# import pandas as pd #引入它主要是为了更好的显示效果
	#s=u'如果给一部古装电影设计服装，必须要考虑故事发生在哪个朝代，汉朝为宽袍大袖，清朝则是马褂旗袍。可在京剧舞台上，几乎任何一个历史人物，根据他的性别年龄、身份地位、基本性格等等，都可以在现有的服饰里找到合适的行头。 '
	#s = u'太阳是一颗恒星'
	#print (keywords(jieba.cut(s)))
	# pd.Series(keywords(jieba.cut(s)))

	mymodel = MyModel('word2vec_wx', 'words')
	print(mymodel.model.wv['吃饭'].shape)
	print(mymodel.predict_proba('吃饭','进食'))
	s = u'广州'
	w = mymodel.relative_words(s)
	print (w[0:5])
