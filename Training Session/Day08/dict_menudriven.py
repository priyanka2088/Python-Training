import pandas as pd

data={'Name':[],'Age':[]}

def add_data():
    name=input("Enter Name : ")
    age=int(input("Enter Age : "))

    data['Name'].append(name)
    data['Age'].append(age)

def return_dataframe():
    return pd.DataFrame(data)    

menu={'1':add_data,'2':return_dataframe}

while(True):
    print("Menu Driven PGM\n1.Add Data into Dictonary\n2.Print dataframe\n3.Exit\n")
    user_choice=input("Enter your Choice : ")
    function_name=menu.get(user_choice)

    if(user_choice=='1'):
        try:
            function_name()
        except Exception as e:
            print("Error Occured")
    elif(user_choice=='2'):
        print("DataFrame : \n",function_name())   
    elif(user_choice=='3'):
        print("Program Exited Successfully")
        break
    else:
        print("Invalid Choice Retry")             