#!/usr/bin/env python
# coding: utf-8

# # Useful Operators
# 
# There are a few built-in functions and "operators" in Python that don't fit well into any category, so we will go over them in this lecture, let's begin!

# ## range
# 
# The range function allows you to quickly *generate* a list of integers, this comes in handy a lot, so take note of how to use it! There are 3 parameters you can pass, a start, a stop, and a step size. Let's see some examples:

# In[1]:


range(0,11)


# Note that this is a **generator** function, so to actually get a list out of it, we need to cast it to a list with **list()**. What is a generator? Its a special type of function that will generate information and not need to save it to memory. We haven't talked about functions or generators yet, so just keep this in your notes for now, we will discuss this in much more detail in later on in your training!

# In[3]:


# Notice how 11 is not included, up to but not including 11, just like slice notation!
list(range(0,11))


# In[4]:


list(range(0,12))


# In[6]:


# Third parameter is step size!
# step size just means how big of a jump/leap/step you 
# take from the starting number to get to the next number.

list(range(0,11,2))


# In[7]:


list(range(0,101,10))


# ## enumerate
# 
# enumerate is a very useful function to use with for loops. Let's imagine the following situation:

# In[8]:


index_count = 0

for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1


# Keeping track of how many loops you've gone through is so common, that enumerate was created so you don't need to worry about creating and updating this index_count or loop_count variable

# In[10]:


# Notice the tuple unpacking!

for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))


# ## zip
# 
# Notice the format enumerate actually returns, let's take a look by transforming it to a list()

# In[12]:


list(enumerate('abcde'))


# It was a list of tuples, meaning we could use tuple unpacking during our for loop. This data structure is actually very common in Python , especially when working with outside libraries. You can use the **zip()** function to quickly create a list of tuples by "zipping" up together two lists.

# In[13]:


mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']


# In[15]:


# This one is also a generator! We will explain this later, but for now let's transform it to a list
zip(mylist1,mylist2)


# In[17]:


list(zip(mylist1,mylist2))


# To use the generator, we could just use a for loop

# In[20]:


for item1, item2 in zip(mylist1,mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))


# ## in operator
# 
# We've already seen the **in** keyword durng the for loop, but we can also use it to quickly check if an object is in a list

# In[21]:


'x' in ['x','y','z']


# In[22]:


'x' in [1,2,3]


# ## min and max
# 
# Quickly check the minimum or maximum of a list with these functions.

# In[26]:


mylist = [10,20,30,40,100]


# In[27]:


min(mylist)


# In[44]:


max(mylist)


# ## random
# 
# Python comes with a built in random library. There are a lot of functions included in this random library, so we will only show you two useful functions for now.

# In[29]:


from random import shuffle


# In[35]:


# This shuffles the list "in-place" meaning it won't return
# anything, instead it will effect the list passed
shuffle(mylist)


# In[36]:


mylist


# In[39]:


from random import randint


# In[41]:


# Return random integer in range [a, b], including both end points.
randint(0,100)


# In[42]:


# Return random integer in range [a, b], including both end points.
randint(0,100)


# ## input

# In[43]:


input('Enter Something into this box: ')

