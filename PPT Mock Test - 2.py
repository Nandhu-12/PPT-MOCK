#!/usr/bin/env python
# coding: utf-8

# # PPT Mock Test

# 1) Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well. You must not use any built-in exponent function or operator. 

# In[5]:



def mySqrt( x: int):
    left=0
    right=10000000
    mid=(left+right)//2
    while(True):
        temp=mid
        if mid*mid>x:
            right=mid+1
        else:
            left=mid
        mid=(left+right)//2
        if temp==mid:
            break
    return left


# In[6]:


print(mySqrt(4))


# In[ ]:




