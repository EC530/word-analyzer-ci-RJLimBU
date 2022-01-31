import sys
#sys.path.append('../word-analyzer-ci-RJLimBU')
from mainloop import wordfreq

def test_islist():
	txt = wordfreq.openfile("example.txt")
	out = wordfreq.rmvpunc(txt)
	name = wordfreq.splitwords(out)
	assert isinstance(name, list)

def test_example1len():
	txt = wordfreq.openfile("example.txt")
	out = wordfreq.rmvpunc(txt)
	name = wordfreq.splitwords(out)
	assert len(name) == 37

def test_example2len():
	txt = wordfreq.openfile("example2.txt")
	out = wordfreq.rmvpunc(txt)
	name = wordfreq.splitwords(out)
	assert len(name) == 136