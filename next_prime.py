# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 11:51:22 2021

@author: shahjahan
"""

def is_prime(x):
    flag=1
    for  i in range(2,x):
        if(x%i==0):
            flag=0
            break
        else:
            flag=1
    if(flag==1):
        return (next_prime(x))
    else:  
        return False
        

def next_prime(x):
    flag=0
    while (flag==0):
        x=x+1
        for i in range(2,x):
            if(x%i==0):
                flag=0
                break
            else:
                flag=1
    if(flag==1):
        return (x)
    
a=int(input("Enter any prime number \t"))
b=is_prime(a)
while(not b):
    print("Sorry, the number you entered is not prime")
    a=int(input("Enter any prime number again \t"))
    b=is_prime(a)
    
print("The next prime number is ",b)
