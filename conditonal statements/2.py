# 2.	Print Grade based on marks
# -	Mark > 90 - print O grade
# -	Mark > 80 - print A grade
# -	Mark > 70 - print B grade
# -	Mark > 60 - print C grade
# -	Mark > 50 - print D grade
# -	Mark < 50 - print fail


mark= int(input("Enter the marks:"))

if (mark >90):
    print("O Grade")
elif (mark >80):
    print("A Grade")
elif (mark >70):
    print("B Grade")
elif (mark >60):
    print("C Grade")
elif (mark >50):
    print("D Grade")
else:
    print("Fail")                
