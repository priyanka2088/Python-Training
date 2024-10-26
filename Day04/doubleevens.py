def double_even(int_list):
    return[2*i if i%2==0 else i for i in int_list]

list1=double_even([2,56, 23,78,93,23,10,12])
print(list1)