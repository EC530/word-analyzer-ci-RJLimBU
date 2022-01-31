import sys
#sys.path.append('../word-analyzer-ci-RJLimBU')
from mainloop import wordfreq

def test_uniqexample1():
	txt = wordfreq.openfile("example.txt")
	out = wordfreq.rmvpunc(txt)
	name = wordfreq.splitwords(out)
	uniq = wordfreq.getwords(name)
	assert len(uniq) == len(set(uniq)) #check if the list only contain unique element

def test_uniqexample2():
	txt = wordfreq.openfile("example2.txt")
	out = wordfreq.rmvpunc(txt)
	name = wordfreq.splitwords(out)
	uniq = wordfreq.getwords(name)
	assert len(uniq) == len(set(uniq)) #check if the list only contain unique element

def test_countwordslen1():
	txt = wordfreq.openfile("example.txt")
	out = wordfreq.rmvpunc(txt)
	name = wordfreq.splitwords(out)
	uniq = wordfreq.getwords(name)
	num = wordfreq.countwords(name, uniq)
	assert len(name) == len(uniq)

def test_countwordslen2():
	txt = wordfreq.openfile("example2.txt")
	out = wordfreq.rmvpunc(txt)
	name = wordfreq.splitwords(out)
	uniq = wordfreq.getwords(name)
	num = wordfreq.countwords(name, uniq)
	assert len(name) == len(uniq)
