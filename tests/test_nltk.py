import sys
#sys.path.append('../word-analyzer-ci-RJLimBU')
from mainloop import wordfreq

NLTK = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", 
		"yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", 
		"they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", 
		"these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", 
		"do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", 
		"of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", 
		"after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", 
		"further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", 
		"few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", 
		"too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

def test_nltktxt():
	txt = wordfreq.openfile("example2.txt")
	out = wordfreq.rmvpunc(txt)
	name = wordfreq.splitwords(out)
	nltk = wordfreq.getwords(name)
	name = wordfreq.rmvNLTK(nltk)

	for ele in NLTK:
		assert not (ele in name)

def test_nltktxt():
	txt = wordfreq.openfile("sample.pdf")
	out = wordfreq.rmvpunc(txt)
	name = wordfreq.splitwords(out)
	nltk = wordfreq.getwords(name)
	name = wordfreq.rmvNLTK(nltk)

	for ele in NLTK:
		assert not (ele in name)
