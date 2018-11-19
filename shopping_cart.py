#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:12:24 2018

@author: Javier
"""
#Our e-shop sells the following products:
#   1. Guitar: $1000
#   2. Pick box: $5
#   3. Guitar Strings: $10
#   Create a function named checkout that takes a list that represents a shopping cart and returns the total cost of it.  This function should check that the shopping cart must not be empty.
#   Create also some tests for the function.  Try to think of the corner cases.
#   Hint: you can represent a product as a dictionary with a name and a price.

#%%
prices = {"Guitar":1000, "Pick Box":5, "Guitar Strings":10}

prices_in_cart = []

def checkout_white(mycart):
    if mycart == []:
        return None
    else:
        for i in mycart: 
#            print(prices_in_cart)
            prices_in_cart.append(prices[i])
                
#            print(prices_in_cart)
    return sum(prices_in_cart)

#checkout_white(["Pick Box", "Guitar"])

#%%

#You want to give more features to the user, so you decide that you will allow 
#them to purchase an insurance package on their purchase and also priority mail.  
#Consider that these two new services can only be purchase once per order.
#
#   1. Insurance: $5
#   2. Priority mail: $10
#
#   Modify your checkout function so it handles these cases correctly, 
#   and add more tests that check your functionality.
    
#%%
    
prices = {"Guitar":1000, "Pick Box":5, "Guitar Strings":10, "Insurance":5, "Priority mail":10}

prices_in_cart = []

def checkout_blue(mycart):
    
    if "Insurance" in mycart:
            prices_in_cart.append(prices["Insurance"])
            
    for i in mycart:
    
        if "Insurance" in mycart:
            
            mycart.pop(mycart.index("Insurance"))
            
            print(mycart)
            
    if "Priority mail" in mycart:
            prices_in_cart.append(prices["Priority mail"])
            
    for i in mycart:
    
        if "Priority mail" in mycart:
            
            mycart.pop(mycart.index("Priority mail"))
            
            print(mycart)
        
    if mycart == []:
        return None
    
    else:
        
        for i in mycart: 

            prices_in_cart.append(prices[i])
            
            print(prices_in_cart)
                
    return sum(prices_in_cart)

#checkout_blue(["Guitar", "Pick Box", "Insurance", "Insurance", "Priority mail", "Priority mail"])
#checkout_blue(["Guitar Strings", "Insurance"])
#checkout_blue(["Insurance", "Insurance", "Guitar", "Insurance", "Insurance"])

#%%

# You want to add a new feature to your ecommerce, you want to create three different 
# tiers of customers:
#
#   - normal: No added benefits
#   - silver: 2% discount on products from the ecommerce
#   - gold: 5% discount on everything
#
#   Modify the checkout function to accept another parameter with the tier of the 
#   customer and apply the discounts as needed.
#
#   Implement this feature in the checkout function and add tests that prove that 
#   your implementation is correct.

prices = {"Guitar":1000, "Pick Box":5, "Guitar Strings":10, "Insurance":5,
          "Priority mail":10} 
tiers = {"Normal": 1, "Silver": 0.98, "Gold": 0.95}

prices_in_cart = []

def checkout_black(tier, mycart):
    
    silver = tiers["Silver"]
    gold = tiers["Gold"]
    normal = tiers["Normal"]
    
    if tier == "Normal":
        silver = 1
        gold = 1
    elif tier == "Silver":
        gold = 1
    elif tier == "Gold":
        silver = 1
        
    print(silver , "Silver")
    print(gold, "Gold")
    print(normal, "Normal")
    
    if "Insurance" in mycart:
            prices_in_cart.append(prices["Insurance"])
            
    for i in mycart:
    
        if "Insurance" in mycart:
            
            mycart.pop(mycart.index("Insurance"))
            
            print(mycart)
            
    if "Priority mail" in mycart:
            prices_in_cart.append(prices["Priority mail"])
            
    for i in mycart:
    
        if "Priority mail" in mycart:
            
            mycart.pop(mycart.index("Priority mail"))
            
            print(mycart)
        
    if mycart == []:
        return None
    
    else:
        
        for i in mycart: 

            prices_in_cart.append(prices[i] * silver)
            
            print(prices_in_cart)
                
    return sum(prices_in_cart) * normal * gold

#checkout_black("Silver", ["Insurance","Pick Box", "Guitar", "Insurance", "Insurance", "Priority mail", "Priority mail"])
#checkout_black("Gold", ["Pick Box", "Insurance", "Insurance", "Priority mail", "Priority mail"])

#%%