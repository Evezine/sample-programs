# 2.Write a Python program to display the examination schedule.
#  (extract the date from     exam_st_date).    exam_st_date = (11, 12, 2014)
#     Sample Output : The examination will start from : 11 / 12 / 2014

 
exam_st_date=(11,12,2014)

# The '%i' placeholders are filled with the values from the 'exam_st_date' tuple

print("The Examination will be start from : %i/%i/%i" % exam_st_date)