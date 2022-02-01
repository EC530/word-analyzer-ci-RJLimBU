#main console
import logging
import matplotlib.pyplot as plt
import PyPDF2
import tracemalloc
import cProfile
#import re

#cProfile.run('re.compile("foo|bar")', 'cProfileStat')

logging.basicConfig(filename = 'mainloop.log', level=logging.INFO,
	format='%(asctime)s:%(levelname)s:%(message)s')

class wordfreq:
	def __init__(self):
		#uniqword = []
		#countword = []
		p = 1

	def getfilepath():
		filepath = input('Please enter path of your file: ')
		logging.info('file name received: {}'.format(filepath))
		return filepath

	def openfile(fp):
		splitchar = "."
		try:
			suf = fp.rsplit(splitchar,1)[1]
		except:
			logging.error('Invalid file name: {}'.format(fp))
			print('Program terminated due to invalid file name.')
			exit()

		logging.info('processing: {}, file type: {}'.format(fp, suf))

		if suf == "txt":
			try:
				f = open(fp,'r')
			except:
				logging.error('unable to open file: {}'.format(fp))
				print("Fail to open file!!!")
				exit()
			txt = f.read()
			f.close()
		elif suf == "pdf":
			try:
				pdfobj = open(fp, 'rb')
			except:
				logging.error('unable to open file: {}'.format(fp))
				print("Fail to open file!!!")
				exit()
			pdfreader = PyPDF2.PdfFileReader(pdfobj)
			pgobj = pdfreader.getPage(0)
			txt = pgobj.extractText()
			pdfobj.close()
		else:
			logging.error('File {}: Format is not txt or pdf.'.format(fp))
			print('Program terminated due to invalid file format.')
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
	logging.info('Contents retrieved from {}: {}'.format(fp, txt))
	txt = wordfreq.rmvpunc(txt)
	logging.info('Punctuation removed: {}'.format(txt))
	txt = wordfreq.splitwords(txt)
	logging.info('Split string to list of words(length={}): {}'.format(len(txt),txt))
	uniqword = wordfreq.getwords(txt) 			#extract distinct words
	logging.info('Distinct words extracted(length={}): {}'.format(len(uniqword),uniqword))
	uniqword = wordfreq.rmvNLTK(uniqword)
	logging.info('NLTK words removed(length={}): {}'.format(len(uniqword),uniqword))
	countword = wordfreq.countwords(txt, uniqword)
	logging.info('word frequency created(length={}): {}'.format(len(countword),countword))

	print("Word Frequency:\n")
	for i in range((len(uniqword))):
		print(uniqword[i]+": "+str(countword[i])+'\n')
		logging.info('{}: {}'.format(uniqword[i], countword[i]))

	wordfreq.plotfreq(uniqword,countword)
	logging.info('Program Done.')

if __name__ == '__main__':
	tracemalloc.start()
	main()
	snapshot = tracemalloc.take_snapshot()
	top_stats = snapshot.statistics('lineno')
	logging.info('Memory Stat(Top 10)')
	#print("[ Top 10 ]")
	for stat in top_stats[:10]:
		logging.info(stat)
		#print(stat)
