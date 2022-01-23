#main console

def getfilepath():
	filepath = input('Please enter path of your file: ')
	return filepath

if __name__ == '__main__':
	print("\n-------------------------------------------\n")
	print("Hello! This is a word analyzer.\n")
	fp = getfilepath()

	print("processing file: %s" % fp)
