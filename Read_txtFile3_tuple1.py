#print ('Hello World!')
#print ('This is my first repo.')

txt = str(input('Enter a line:- '))

words = txt.split()
t = list()
print (type, t)
for word in words:
	t.append((len(word), word)) # builds a list of tuples - each tuple contain the the word and its length
print (t)

t.sort() # increasing order of length
print (t)

t.sort(reverse = True) # decresing order
print (t)

words_only = list()
len_only = list()
for length, word in t:
	words_only.append(word)
	len_only.append(length)
print('words:- ', words_only)
print('length:- ', len_only)