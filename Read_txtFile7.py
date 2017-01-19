import string
fname = input('Enter the file name: ')
print('\n')

# Opening a file
try:
	fhand = open(fname)
except:
	print('File cannot opened:' , fname)
	exit()

# Reading a file, counting words using dictionary

counting_words = dict() #Assigning a dictionary

str_input = input('enter words that you want to search in this file: ')
str_input = str_input.lower()
spec_words = list()
spec_words = str_input.split()

#spec_words = ['president', 'bush']
special = {}.fromkeys(spec_words,0)

for line in fhand:
	line = line.rstrip()
	line = line.translate(line.maketrans('', '', string.punctuation)) #remove punctuations
	line = line.lower() #transfer upper to lower case
	words = line.split()
		
	for word in words:
		if word in spec_words:
			special[word] +=1

lst_spewords = list(special.keys())

for key in lst_spewords:
	print(key, special[key])