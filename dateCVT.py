import sys
sys.stdout.write("Enter the date(format: mmddyyyy ):")
a=int(raw_input())
month=a/1000000                        #month input
date=(a-(month*1000000))/10000          #date input
year=(a-date*10000-month*1000000)     #year input
if(date>31 or date<0):                #date check
    print("Wrong date input!!!")
elif(month==1):  #january
    if(date<=31):
        print("January/"+str(date)+"/"+str(year))
    else : print("Wrong date input !!!")
elif(month==2):                         #feb
    if(date>0 and date<=29):
        print("February/"+str(date)+"/"+str(year))
    else: print("Wrong date input!!!")
elif(month==3): #march
    if(date<=31):

        print("March/"+str(date)+"/"+str(year))
    else: print("Wrong date input!!!")
elif (month == 4):#april
    if(date<=30):
        print("April/" + str(date)+"/" + str(year))
    else:print("Wrong date input!!!")
elif(month==5):#may
    if(date<=31):
        print("May/"+str(date)+"/"+str(year))
    else:print("Wrong date input!!!")
