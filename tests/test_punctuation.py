import sys
#sys.path.append('../word-analyzer-ci-RJLimBU')
from mainloop import wordfreq

def test_rmvpunc():
	txt = wordfreq.openfile("example.txt")
	name = wordfreq.rmvpunc(txt)
	punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''
	for i in range(len(name)):
		assert name[i] not in punc

def test_openexample2():
	txt = wordfreq.openfile("example2.txt")
	name = wordfreq.rmvpunc(txt)
	punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''
	for i in range(len(name)):
		assert name[i] not in punc