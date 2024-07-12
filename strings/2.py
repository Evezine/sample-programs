#2.	Python program to print even length words in a string

def even_length_word(s):
    word=s.split()
    for word in word:
        if len(word)% 2==0:
            print(word,end=" ")

s="this is a very dangerous one so dont do it with intention"
even_length_word(s)            