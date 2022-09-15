# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:37:11 2022

@author: Trent
"""

import math
import sys
import random

# class PublicUser:
#     public_key = ""
#     private_key = ""
    
# Use Fermat's Little Theorem for parameters of pow() to gen p & q
# Large prime numbers for testing; from https://bigprimes.org/
p_val = 26699618156112777433
q_val = 16464747126412153627
n = p_val * q_val
phi = (p_val - 1) * (q_val - 1)
e = random.randrange(1000000, phi) # relatively prime to phi; encryption key
    
while not math.gcd(e, phi) == 1:
    e = random.randrange(1000000, phi)

print(e)

def encrypted_message():
    #create a dictionary to store more than one message?
    pass
    
def sign_message(sign):
    #I guess we just create a variable for the signature?
    pass
    
def public_user():
    ans = int(input("\nAs a public user, what would you like to do?\n" +
                    "1. Send an encrypted message.\n" +
                    "2. Authenticate a digital signature.\n" + 
                    "3. Exit.\n" +
                    "\n Enter your choice: "))
    
    if ans == 1:
        message = input("\nEnter a message: ")
        #call funtion to encrypt a message (message)
    elif ans == 2:
        #call funtion to authenticate a digital signature
        pass
    elif ans == 3:
        sys.exit("Goodbye.")
    else:
        print("Invalid choice.")
        public_user()
    
def owner():
    ans = int(input("\nAs the owner of the keys, what would you like to do?\n" +
                    "1. Decrypt a received message.\n" +
                    "2. Digitally sign a message.\n" +
                    "3. Exit.\n" +
                    "\nEnter your choice: "))
    if ans == 1:
        #call function to list encrypted messages
        print("\nThe following messages are available:\n\t")
    elif ans == 2:
        #call function to signs a message
        sig = input("\nEnter a message: ")
        sign_message(sig)
    elif ans == 3:
        sys.exit("Goodbye.")
    else:
        print("Invalid choice.")
        owner()
        
def prompt():
    ans = int(input("Please select your user type\n" +
          "1. A public user.\n" +
          "2. The owner of the keys.\n" +
          "3. Exit program\n" +
          "\nEnter your choice: "))
    
    if ans == 1:
        public_user()
    elif ans == 2:
        owner()
    elif ans == 3:
        sys.exit("Goodbye.")
    else:
        print("Invalid choice.")
        prompt()

prompt()
