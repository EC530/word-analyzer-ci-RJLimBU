import sys
#sys.path.append('../word-analyzer-ci-RJLimBU')
from mainloop import wordfreq

def test_openfile():
	name = wordfreq.openfile("example.txt")
	for i in range(len(name)):
		assert isinstance(name[i],str)
