#!/usr/bin/env python
# coding: utf-8

# # Object Oriented Programming
# ## Homework Assignment
# 
# #### Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

# In[1]:


class Line:
    
    def __init__(self,coor1,coor2):
        pass
    
    def distance(self):
        pass
    
    def slope(self):
        pass


# In[2]:


# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)


# In[3]:


li.distance()


# In[4]:


li.slope()


# ________
# #### Problem 2

# Fill in the class 

# In[5]:


class Cylinder:
    
    def __init__(self,height=1,radius=1):
        pass
        
    def volume(self):
        pass
    
    def surface_area(self):
        pass


# In[6]:


# EXAMPLE OUTPUT
c = Cylinder(2,3)


# In[7]:


c.volume()


# In[8]:


c.surface_area()

