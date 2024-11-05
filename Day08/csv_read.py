def datagetter(file_handle,college_name_param):
    #logic
    counts={}
    for line in file_handle:
        #print(line)
        line=line[:-1:]
        line_list=line.split(',')
        #print(line_list)
        college_name=line_list[1]
        #if(college_name=="College C"):
        # if(college_name==college_name_param):
        #     #print(college_name)
        #     print(line)
        if college_name not in counts:
            counts[college_name]=1
        else:
            counts[college_name]=+1

    print(counts)    

file_handle=open(r'C:\Users\Administrator\Documents\UST Training\Python-Training\Day08\data.csv','r')

datagetter(file_handle,"College C")

file_handle.close()    