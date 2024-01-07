import math
import os
import random
import re
import sys


n= int(input("What is the integer?: "))
if (n%2!=0) or (6<=n<=20 and n%2==0): 
    print("Weird")
elif (n%2==0 and 2<=n<=5) or (n>20 and n%2==0):
    print("Not Weird") 
else:
    print("Error! Please enter an integer")    
       