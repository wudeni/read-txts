import string
fname = input('Enter the file name: ')
print('\n')

# Opening a file
try:
	fhand = open(fname)
except:
	print('File cannot opened:' , fname)
	exit()


counting_words = dict()

for line in fhand:
	line = line.rstrip()
	line = line.translate(line.maketrans('', '', string.punctuation)) #remove punctuations
	line = line.lower() #transfer upper to lower case
	words = line.split()
	for word in words:
		if word not in counting_words:
			counting_words[word] = 1
		else:
			counting_words[word] += 1
			

t = list()
for key, val in list(counting_words.items()):
	t.append((val, key))

t.sort(reverse = True) # decresing order
print('tuple modified: words and decreasing order of count')
print (t)
print('\n')	

words_only = list()
len_only = list()
for length, word in t[:10]:
	words_only.append(word)
print('the first ten most common words in the current file are:-\n', words_only)
#OR
for key,value in t[:10]:
	print(key, value)
