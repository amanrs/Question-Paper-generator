with open("question paper.txt",'w',encoding = 'utf-8') as f:
    f.write("Question Paper \n")
    f.write("Lesson included are {}\n\n".format(chapter_list))
    f.write("Section A\n")
    
    # section_a.groupby("Priority")
    for ques in section_a["Questions"]:
        f.write("{}\n".format(ques))
    f.write("\n\nSection B\n")
    for ques in section_b["Questions"]:
        f.write("{}\n".format(ques))
    f.write("\n\nSection C\n")
    for ques in section_c["Questions"]:
        f.write("{}\n".format(ques))
    f.write("\n\nSection D\n")
    for ques in section_d["Questions"]:
        f.write("{}\n".format(ques))