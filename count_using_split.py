words=input('Enter a string : ')
word=words.split()
word_count={}
for word in words:
    word_count[word]=word_count.get(word,0)+1
print(word_count)