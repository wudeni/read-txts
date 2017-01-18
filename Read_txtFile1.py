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
count_lines = 0
tot_words = 0
distinct_count = 0

for line in fhand:
	line = line.rstrip()
	line = line.translate(line.maketrans('', '', string.punctuation)) #remove punctuations
	line = line.lower() #transfer upper to lower case
	count_lines = count_lines + 1 #counting lines
	words = line.split()
	for word in words:
		tot_words +=1
		if word not in counting_words:
			counting_words[word] = 1
		else:
			counting_words[word] += 1
			distinct_count += 1

print('The list of words: ', words, '\n', 'Total words:', tot_words, '\n' )
print('..........................................')
print('There are ', count_lines, ' lines in the file ', fname, '\n')
print('..........................................')
print('The dictionary - ', counting_words, '\n')
print('..........................................')
print('There are ', distinct_count, ' of distinct words.\n')	