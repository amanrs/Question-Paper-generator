i = 0
for value in priority_values:
    ques_a = questions_a[questions_a["Priority"]==value]
    if(a_ques<=ques_a["Index"].count()):
        section_a = ques_a.sample(a_ques)
        
        break
    else:
        if section_a.empty:
            section_a = ques_a.sample(ques_a["Index"].count())
        else:
            section_a.merge(ques_a.sample(ques_a["Index"].count()),how='outer')
        print("values = {} : {}".format(value,section_a["Priority"]))
        i+=1
print(section_a)
