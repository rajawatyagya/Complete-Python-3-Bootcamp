#!/usr/bin/env python
# coding: utf-8

# # Timing your code
# Sometimes it's important to know how long your code is taking to run, or at least know if a particular line of code is slowing down your entire project. Python has a built-in timing module to do this. 
# 
# This module provides a simple way to time small bits of Python code. It has both a Command-Line Interface as well as a callable one. It avoids a number of common traps for measuring execution times. 
# 
# Let's learn about timeit!

# In[1]:


import timeit


# Let's use timeit to time various methods of creating the string '0-1-2-3-.....-99'
# 
# We'll pass two arguments: the actual line we want to test encapsulated as a string and the number of times we wish to run it. Here we'll choose 10,000 runs to get some high enough numbers to compare various methods.

# In[2]:


# For loop
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)


# In[3]:


# List comprehension
timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)


# In[4]:


# Map()
timeit.timeit('"-".join(map(str, range(100)))', number=10000)


# Great! We see a significant time difference by using map()! This is good to know and we should keep this in mind.
# 
# Now let's introduce iPython's magic function **%timeit**<br>
# *NOTE: This method is specific to jupyter notebooks!*
# 
# iPython's %timeit will perform the same lines of code a certain number of times (loops) and will give you the fastest performance time (best of 3).
# 
# Let's repeat the above examinations using iPython magic!

# In[5]:


get_ipython().run_line_magic('timeit', '"-".join(str(n) for n in range(100))')


# In[6]:


get_ipython().run_line_magic('timeit', '"-".join([str(n) for n in range(100)])')


# In[7]:


get_ipython().run_line_magic('timeit', '"-".join(map(str, range(100)))')


# Great! We arrive at the same conclusion. It's also important to note that iPython will limit the amount of *real time* it will spend on its timeit procedure. For instance if running 100000 loops took 10 minutes, iPython would automatically reduce the number of loops to something more reasonable like 100 or 1000.
# 
# Great! You should now feel comfortable timing lines of your code, both in and out of iPython. Check out the documentation for more information:
# https://docs.python.org/3/library/timeit.html
