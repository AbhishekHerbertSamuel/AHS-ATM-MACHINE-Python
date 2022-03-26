#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 17:07:24 2022

@author: abhishekherbertsamuel
"""
# For this purpose assume that the account has a balance of 2 Lakh Rupees.
import sys
def pin(atmpin):
   count=0
   for i in atmpin:
       if (i.isdigit()==True):
           count+=1
   if (count>4 or count<4):
       print("The pin that you entered is not valid. Please try again with a valid pin.")
       sys.exit()
   else:
       print("Option to Withdraw an Amount:")
       print("Option to Check Account Balance:")
       select()
def select():
    print("Which option would you like to select from the above two?Enter either of the above phrases exactly as given.")
    x=input()
    if(x=="Option to Withdraw an Amount:"):
        withdraw()
    elif(x=="Option to Check Account Balance:"):
        check()
    else:
        print("Enter the above phrases with : as they are displayed.Please try again.")
        sys.exit()
def withdraw():
    balance=200000
    y=int(input("Enter the amount you wish to withdraw:"))
    if (y<100):
        print("The minimum amount that you can withdraw is 100 rupees.Please try again.")
        sys.exit()
    balance=balance-y
    print("The remaining amount in your account after withdrawal of",y,"rupees is:",balance,"rupees")
    print("Thank you for using ABC Bank.Looking forward to seeing you again.")
def check():
   balance=200000    
   print("Your account balance currently is:",balance,"rupees")
   print("\n If you wish to withdraw money enter the phrase Yes below exactly as it is written:")
   a=input()
   if(a=="Yes"):
       withdraw()
   else:
       print("Thank you for using ABC Bank.Looking forward to seeing you again.")
atmpin=(input("Enter you 4 digit PIN:"))
pin(atmpin)

       
    
    
