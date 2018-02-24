# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:36:27 2018

@author: Subba Reddy Chaganti   
"""

#Sample if condition
Marks = int(input("Please Enter Student Marks:"))

if(Marks > 80):
    print("Gread A")
elif((Marks > 60) and (Marks <=80)):
    print("Gread B")
elif((Marks > 40) and (Marks <= 60)):
    print("Gread C")
else:
    print("Gread D")
