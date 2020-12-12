#os is preinstalled in system
#I try it on terminal
import os

#os.chdir('/home/fuck') ###chdir is used to changed the directory
#os.getcwd() #so check getcwd()n function is used to get the workng  directory

#os.mkdir('try')  #In Order To Make New Directory Or You Can Try It With Specific Location 
#os.chdir('try')   #Now Try To Change Your Directory Which You Make 
#os.getcwd()  #Now Check The Working Directory

#os.listdir()   #This Function is used to List All The Directory in Working 


def function():
    change = os.chdir('/home/fuck/Downloads')
    make = os.mkdir('swing')

    print(os.listdir())
    print(os.getcwd())
function()
