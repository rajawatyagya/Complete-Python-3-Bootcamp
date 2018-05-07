#!/usr/bin/env python
# coding: utf-8

# # Python Debugger
# 
# You've probably used a variety of print statements to try to find errors in your code. A better way of doing this is by using Python's built-in debugger module (pdb). The pdb module implements an interactive debugging environment for Python programs. It includes features to let you pause your program, look at the values of variables, and watch program execution step-by-step, so you can understand what your program actually does and find bugs in the logic.
# 
# This is a bit difficult to show since it requires creating an error on purpose, but hopefully this simple example illustrates the power of the pdb module. <br>*Note: Keep in mind it would be pretty unusual to use pdb in an iPython Notebook setting.*
# 
# ___
# Here we will create an error on purpose, trying to add a list to an integer

# In[1]:


x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)
result2 = y+x
print(result2)


# Hmmm, looks like we get an error! Let's implement a set_trace() using the pdb module. This will allow us to basically pause the code at the point of the trace and check if anything is wrong.

# In[ ]:


import pdb

x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)

# Set a trace using Python Debugger
pdb.set_trace()

result2 = y+x
print(result2)


# Great! Now we could check what the various variables were and check for errors. You can use 'q' to quit the debugger. For more information on general debugging techniques and more methods, check out the official documentation:
# https://docs.python.org/3/library/pdb.html
