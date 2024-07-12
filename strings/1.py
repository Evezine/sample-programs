# #1.	Reverse the words in the given string program using
# i.	Loop 
# ii.	Stack
# iii.	Reverse method
# iv.	slicing

'''
#using loop

def reverse(sentence):
    word =sentence.split()
    reverse_sentence=""
    for word in reversed(word):
        reverse_sentence+= word+" "
    return reverse_sentence.strip()

sentence=str(input("Enter the string:"))
print(reverse(sentence))   ''' 
'''
# using reverse method

def reverse(sentence):
    word=sentence.split()
    word.reverse()#reverse func
    return" ".join(word)

sentence="give me a pen"
print(reverse(sentence)) '''

'''#using slicing method

def reverse(sentence):
    word= sentence.split()#to split the words firstly
    return" ".join(word[::-1])
sentence="he is riding cycle"
print(reverse(sentence))'''

#using stack

def reverse(sentence):
    word=sentence.split()
    stack=[]
    for word in word:
        stack.append(word)
    reverse_sentence =""
    while stack:
            reverse_sentence+=stack.pop()+" "
    return reverse_sentence.strip()
        
sentence="he is riding cycle"
print(reverse(sentence))        