# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:42:36 2020

@author: Amarnath
"""
import os

"""
myfile=open("myfile.txt","w")

#mystr = input("Enter anything : ")

while (mystr != "@"):
    myfile.write(mystr+"\n")
    mystr = input("Enter anything to write to file, @ to quit : ")
    
myfile.close()
"""
myfile=open("myfile.txt","r")
print(myfile.read())    

myfile.close()

if (os.path.isfile("E:/anitha/py-programs/myfile.txt")):
    print("File exists")
else:
    print("testing")
    
if (os.path.isfile("E:/anitha/py-programs/myfile1.txt")):
    print("Nooo")
else:    
    print("File doesn't exists")    
    
with open('myfile.txt') as f:
    print(f.read())
    
if(f.closed):
    print("yeah, its closed automatically")
    
#readline - reads line by line
    
myfile=open("myfile.txt","r")
print("Line 1 is ",myfile.readline())        

print("Line 2 is ",myfile.readline())        

print("Line 3 is ",myfile.readline())   



for line in myfile:
    print(line, end='') 
    
myfile.close()


