#!/usr/bin/env python
# coding: utf-8

# # complex()
# 
# complex() returns a complex number with the value real + imag*1j or converts a string or number to a complex number. 
# 
# If the first parameter is a string, it will be interpreted as a complex number and the function must be called without a second parameter. The second parameter can never be a string. Each argument may be any numeric type (including complex). If imag is omitted, it defaults to zero and the constructor serves as a numeric conversion like int and float. If both arguments are omitted, returns 0j.
# 
# If you are doing math or engineering that requires complex numbers (such as dynamics, control systems, or impedance of a circuit) this is a useful tool to have in Python.
# 
# Let's see some examples:

# In[1]:


# Create 2+3j
complex(2,3)


# In[2]:


complex(10,1)


# We can also pass strings:

# In[3]:


complex('12+2j')


# That's really all there is to this useful function. Keep it in mind if you are ever dealing with complex numbers in Python!
