#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 14:22:35 2018

@author: Javier
"""

from shopping_cart import checkout_white
from shopping_cart import checkout_blue
from shopping_cart import checkout_black


#def test_checkout_white_empty_list():
#    mylist = []
#    
#    for case in mylist:
#        assert checkout_white(mylist) == None
#        
#        
#def test_checkout_white_one_item_in_mylist():
#    mylist = ["Guitar"]
#    
#    for case in mylist:
#        assert checkout_white(mylist) == 1000
#        
#def test_checkout_blue_empty_list():
#    mylist = []
#    
#    for case in mylist:
#        assert checkout_blue(mylist) == None
#
#def test_checkout_blue_two_insurances():
#    mylist = ["Guitar Strings", "Insurance", "Insurance"]
#    
#    for case in mylist:
#        assert checkout_blue(mylist) == 15
#
#def test_checkout_blue_three_insurance_in_different_order():
#    mylist = ["Insurance", "Guitar", "Insurance", "Insurance"]
#    
#    for case in mylist:
#        assert checkout_blue(mylist) == 1005
#        
#def test_checkout_black_silver():
#    
#    mycart = ["Guitar"]
#    
#    for case in mycart:
#        assert checkout_black("Silver",mycart) == 980
#
#
#def test_checkout_black_gold():
#    
#    mycart = ["Pick Box", "Insurance", "Insurance", "Priority mail", "Priority mail"]
#    
#    for case in mycart:
#        assert checkout_black("Gold",mycart) == 19
##        
#
