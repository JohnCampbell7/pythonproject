'''
Created on 24 Feb 2019

@author: user
'''
from ctypes.test.test_pickling import name


def sayhi(name, age):
    print("Hello " + name + ", you are " + age)

  
sayhi("Mike", "35")
sayhi("John", "70")

