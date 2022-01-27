#main console
import matplotlib.pyplot as plt
#import numpy as np

class wordfreq:
	def __init__(self):
		#uniqword = []
		#countword = []
		a = 0

	def getfilepath():
		filepath = input('Please enter path of your file: ')
		return filepath

	def openfile(fp):
		f = open(fp,'r')
		txt = f.read()
		txt = txt.split()
		f.close()
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
	print(len(txt))
	uniqword = wordfreq.getwords(txt)

	countword = wordfreq.countwords(txt, uniqword)

	print(len(uniqword))
	print(len(countword))
	wordfreq.plotfreq(uniqword,countword)
	#print("Please enter a valid path!!!")

if __name__ == '__main__':
	main()
