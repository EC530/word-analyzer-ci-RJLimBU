#main console
import matplotlib.pyplot as plt
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
		f = open(fp,'r')
		txt = f.read()
		#txt = txt.split()
		f.close()
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

	countword = wordfreq.countwords(txt, uniqword)

	print("Word Frequency:\n")
	for i in range((len(uniqword))):
		print(uniqword[i]+": "+str(countword[i])+'\n')

	wordfreq.plotfreq(uniqword,countword)
	#print("Please enter a valid path!!!")

if __name__ == '__main__':
	main()
