import pandas as pd
import numpy as np


"""
Get the excel file for Questions
"""
examfile = pd.read_excel('ex1.xlsx')
print(examfile.head(10))

 
"""
A function to select the chapter
""" 
chapternames = examfile['Chapter Name'].unique()
print("Please select from the following chapters")
i = 1
for chapters in chapternames:
    print("{}. {}".format(i,chapters))
    i= i+1
selected_chaps = input("Please input the unit number of the chapters (for multiple chapters add them with the help of ',' like this- 1,4,5): -")
print("You selected these chapters : -")
selected_chaps = selected_chaps.split(",")
selected_chaps = [int(chap) for chap in selected_chaps]
i = 1
chapter_list = []
for chapter in selected_chaps:
    print("{}. {}".format(i,chapternames[chapter-1]))
    chapter_list.append(chapternames[chapter-1])
    i= i+1
#get the dataframe with these chapternames
exam_sheet_qb = pd.DataFrame()
for ch in chapter_list:
    exam_sheet_qb = pd.concat([exam_sheet_qb, examfile[examfile["Chapter Name"] == ch]], axis=0)
print(exam_sheet_qb.shape)
questions_a, questions_b, questions_c, questions_d = exam_sheet_qb[exam_sheet_qb["marks"]==2],exam_sheet_qb[exam_sheet_qb["marks"]==3],exam_sheet_qb[exam_sheet_qb["marks"]==4],exam_sheet_qb[exam_sheet_qb["marks"]==6]
print(questions_a.shape[0], questions_b.shape[0], questions_c.shape[0], questions_d.shape[0])
no_of_ques_mean = (questions_a.shape[0] + questions_b.shape[0] + questions_c.shape[0] + questions_d.shape[0])/4
avg_questions = int(no_of_ques_mean/2)
total_possible_marks = questions_a.shape[0] * 2 + questions_b.shape[0] * 3 + questions_c.shape[0] * 4 + questions_d.shape[0] * 6
print("total possible marks: {} \nvs calculated marks:".format(total_possible_marks))
total_marks = avg_questions * 2 + avg_questions * 3 + avg_questions * 4 + avg_questions * 6
is_10_multiple = total_marks%10
total_marks = total_marks - is_10_multiple
# percentage_a = questions_a.shape[0]*2/total_possible_marks
# percentage_b = questions_b.shape[0]*3/total_possible_marks
# percentage_c = questions_c.shape[0]*4/total_possible_marks
# percentage_d = questions_d.shape[0]*6/total_possible_marks

# print("percentage of a is {} and its marks acquicition is {}".format(percentage_a*100,int(total_marks*percentage_a)+1))
# print("percentage of b is {} and its marks acquicition is {}".format(percentage_b*100,int(total_marks*percentage_b)))
# print("percentage of c is {} and its marks acquicition is {}".format(percentage_c*100,int(total_marks*percentage_c)))
# print("percentage of d is {} and its marks acquicition is {}".format(percentage_d*100,int(total_marks*percentage_d)))
print(total_marks)
mark_acq_d = int((questions_d.shape[0]/2)*6)
d_ques = int(questions_d.shape[0]/2)
mark_acq_c = int((questions_c.shape[0]/2)*4)
c_ques = int(questions_c.shape[0]/2)
mark_acq_b = int((questions_b.shape[0]/2))
if(mark_acq_b%2!=0):
    mark_acq_b = mark_acq_b -1
b_ques = mark_acq_b
mark_acq_b = mark_acq_b * 3
tot = mark_acq_b + mark_acq_c + mark_acq_d
mark_acq_a = int(total_marks - tot)
a_ques = int(mark_acq_a/2)
print("{} {} {} {}".format(a_ques,b_ques,c_ques,d_ques))
# section_a = questions_a.sample(a_ques)
# section_b = questions_b.sample(b_ques)
# section_c = questions_c.sample(c_ques)
# section_d = questions_d.sample(d_ques)
priority_values = questions_a["Priority"].unique()
priority_values = -np.sort(-priority_values)
# print(questions_a["Priority"].value_counts())
print("\n\n\n\n")
section_a = pd.DataFrame()
i = 0
for value in priority_values:
    ques_a = questions_a[questions_a["Priority"]==value]
    print(ques_a)
    print("\n")
    if(a_ques<=ques_a["Index"].count()):
        section_a = ques_a.sample(a_ques)
        print("It comes to this")
        # print("values = {} : {}".format(i,section_a["Priority"]))
        break
    else:
        if section_a.empty:
            print("The df is empty\n")
            section_a = ques_a.sample(ques_a["Index"].count())
        else:
            section_a.append(ques_a.sample(ques_a["Index"].count()))
        # print("values = {} : {}".format(value,section_a["Priority"]))
        i+=1
print("this is the dataframe :\n{}".format(section_a))

