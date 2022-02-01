import sys
#sys.path.append('../word-analyzer-ci-RJLimBU')
from mainloop import wordfreq

def test_openexample1():
	name = wordfreq.openfile("example.txt")
	txt = "hello, this is an example txt file to read\nI wandered lonely as a cloud\nThat floats on high over vales and hills\nWhen all at once I saw a crowd\nA host of golden worker ants.\n"
	for i in range(len(name)):
		assert name[i] == txt[i]

def test_openexample2():
	name = wordfreq.openfile("example2.txt")
	assert name[0] == 'B'
	assert name[-1] == '!'

def test_openpdf():
	name = wordfreq.openfile("sample.pdf")
	assert name[0] == 'A'
