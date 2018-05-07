#!/usr/bin/env python
# coding: utf-8

# # Object Oriented Programming
# ## Homework Assignment
# 
# #### Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

# In[1]:


class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)


# In[2]:


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
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.height*3.14*(self.radius)**2
    
    def surface_area(self):
        top = 3.14 * (self.radius)**2
        return (2*top) + (2*3.14*self.radius*self.height)


# In[6]:


c = Cylinder(2,3)


# In[7]:


c.volume()


# In[8]:


c.surface_area()

