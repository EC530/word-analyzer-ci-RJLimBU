#main console
import matplotlib.pyplot as plt
import PyPDF2
#import numpy as np


class wordfreq:
	def __init__(self):
		#uniqword = []
		#countword = []
		p = 1

	def getfilepath():
		filepath = input('Please enter path of your file: ')
		return filepath

	def openfile(fp):
		splitchar = "."
		try:
			suf = fp.rsplit(splitchar,1)[1]
		except:
			print("Please enter valid file name!\n")
			print(exit)
			exit()
		if suf == "txt":
			f = open(fp,'r')
			txt = f.read()
			#txt = txt.split()
			f.close()
		elif suf == "pdf":
			pdfobj = open(fp, 'rb')
			pdfreader = PyPDF2.PdfFileReader(pdfobj)
			pgobj = pdfreader.getPage(0)
			txt = pgobj.extractText()
			pdfobj.close()
		else:
			print("Format should be txt or pdf!")
			print(exit)
			exit()
		return txt

	def rmvpunc(txt):
		punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''
		out = txt
		for i in out:
			if i in punc:
				out = out.replace(i, "")

		return out

	def splitwords(out):
		txt = out.split()
		return txt

	def getwords(txt):
		uniquewords = []
		for word in txt:
			if word not in uniquewords:
				uniquewords.append(word)

		return uniquewords

	def rmvNLTK(uniqword):
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

		out = uniqword

		for ele in NLTK:
			if ele in out:
				out.remove(ele)

		return out

	def countwords(txt, uniquewords):
		l = len(uniquewords)
		count = []
		for i in range(l):
			count.append(txt.count(uniquewords[i]))

		return count

	def plotfreq(uniqword, countword):
		plt.bar(uniqword, countword, align = 'center')
		plt.xlabel('Words')
		plt.ylabel('Frequency')
		plt.xticks(rotation = 'vertical')
		plt.show()

def main():
	print("\n-------------------------------------------\n")
	print("Hello! This is a word analyzer.\n")
	fp = wordfreq.getfilepath()
	print("\n-----------processing file: %s-----------\n" % fp)

	txt = wordfreq.openfile(fp)
	txt = wordfreq.rmvpunc(txt)
	txt = wordfreq.splitwords(txt)
	#print(len(txt))
	uniqword = wordfreq.getwords(txt)
	uniqword = wordfreq.rmvNLTK(uniqword)

	countword = wordfreq.countwords(txt, uniqword)

	print("Word Frequency:\n")
	for i in range((len(uniqword))):
		print(uniqword[i]+": "+str(countword[i])+'\n')

	wordfreq.plotfreq(uniqword,countword)
	#print("Please enter a valid path!!!")

if __name__ == '__main__':
	main()
