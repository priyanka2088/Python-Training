import win32api
import win32com.client
import win32gui




def custom_messagebox():
    result = win32gui.MessageBox(0,"Hello Manu do you like Python?","Custom Question",1)
    print(result)

    if(result==1):
        win32gui.MessageBox(0,"Thanks!! you love Python?","Info",1)
    elif(result==2):
        win32gui.MessageBox(0,"Oops!! sorry","Info",1)        

custom_messagebox()