import string
fname = input('Enter the file name: ')
print('\n')

# Opening a file
try:
	fhand = open(fname)
except:
	print('File cannot opened:' , fname)
	exit()

t = list()

for line in fhand:
	line = line.rstrip()
	line = line.translate(line.maketrans('', '', string.punctuation)) #remove punctuations
	line = line.lower() #transfer upper to lower case
	words = line.split()
	for word in words:
		t.append((len(word), word)) # builds a list of tuples - each tuple contain the the word and its length
print('tuple un-modified: words and length')
print (t)
print('\n')

t.sort(reverse = True) # decresing order
print('tuple modified: words and decreasing order of length')
print (t)
print('\n')

words_only = list()
#len_only = list()
for length, word in t:
	words_only.append(word)
	#len_only.append(length)

print('words:-\n', words_only)
#print('length of the words:-\n', len_only)
