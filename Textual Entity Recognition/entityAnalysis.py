import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm

nlp = en_core_web_sm.load()

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent


f = open("moana.txt", encoding="utf8")
x = (f.read())

script = x.split("\n")

scriptList = []

for line in script:
	if (": " in line):
		L = line.find(": ")
		scriptList.append(line[L+1:])


wholeMovieEnties =[]
for sentence in scriptList:
	entityDic = {}

	phrase = nlp(sentence)
	# pprint([(X, X.ent_iob_, X.ent_type_) for X in phrase])
	for x in phrase:
		if ((x.ent_iob_ != "O") and (x not in entityDic)):
			entityDic[x] = x.ent_type_

	wholeMovieEnties.append(entityDic)


print(wholeMovieEnties)
