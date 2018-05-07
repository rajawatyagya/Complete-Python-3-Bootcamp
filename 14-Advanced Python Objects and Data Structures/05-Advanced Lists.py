#!/usr/bin/env python
# coding: utf-8

# # Advanced Lists
# 
# In this series of lectures we will be diving a little deeper into all the methods available in a list object. These aren't officially "advanced" features, just methods that you wouldn't typically encounter without some additional exploring. It's pretty likely that you've already encountered some of these yourself!
# 
# Let's begin!

# In[1]:


list1 = [1,2,3]


# ## append
# You will definitely have used this method by now, which merely appends an element to the end of a list:

# In[2]:


list1.append(4)

list1


# ## count
# We discussed this during the methods lectures, but here it is again. <code>count()</code> takes in an element and returns the number of times it occurs in your list:

# In[3]:


list1.count(10)


# In[4]:


list1.count(2)


# ## extend
# Many times people find the difference between extend and append to be unclear. So note:
# 
# **append: appends whole object at end:**

# In[5]:


x = [1, 2, 3]
x.append([4, 5])
print(x)


# **extend: extends list by appending elements from the iterable:**

# In[6]:


x = [1, 2, 3]
x.extend([4, 5])
print(x)


# Note how <code>extend()</code> appends each element from the passed-in list. That is the key difference.

# ## index
# <code>index()</code> will return the index of whatever element is placed as an argument. Note: If the the element is not in the list an error is raised.

# In[7]:


list1.index(2)


# In[8]:


list1.index(12)


# ## insert 
# <code>insert()</code> takes in two arguments: <code>insert(index,object)</code> This method places the object at the index supplied. For example:

# In[9]:


list1


# In[10]:


# Place a letter at the index 2
list1.insert(2,'inserted')


# In[11]:


list1


# ## pop
# You most likely have already seen <code>pop()</code>, which allows us to "pop" off the last element of a list. However, by passing an index position you can remove and return a specific element.

# In[12]:


ele = list1.pop(1)  # pop the second element


# In[13]:


list1


# In[14]:


ele


# ## remove
# The <code>remove()</code> method removes the first occurrence of a value. For example:

# In[15]:


list1


# In[16]:


list1.remove('inserted')


# In[17]:


list1


# In[18]:


list2 = [1,2,3,4,3]


# In[19]:


list2.remove(3)


# In[20]:


list2


# ## reverse
# As you might have guessed, <code>reverse()</code> reverses a list. Note this occurs in place! Meaning it affects your list permanently.

# In[21]:


list2.reverse()


# In[22]:


list2


# ## sort
# The <code>sort()</code> method will sort your list in place:

# In[23]:


list2


# In[24]:


list2.sort()


# In[25]:


list2


# The <code>sort()</code> method takes an optional argument for reverse sorting. Note this is different than simply reversing the order of items.

# In[26]:


list2.sort(reverse=True)


# In[27]:


list2


# ## Be Careful With Assignment!
# A common programming mistake is to assume you can assign a modified list to a new variable. While this typically works with immutable objects like strings and tuples:

# In[28]:


x = 'hello world'


# In[29]:


y = x.upper()


# In[30]:


print(y)


# This will NOT work the same way with lists:

# In[31]:


x = [1,2,3]


# In[32]:


y = x.append(4)


# In[33]:


print(y)


# What happened? In this case, since list methods like <code>append()</code> affect the list *in-place*, the operation returns a None value. This is what was passed to **y**. In order to retain **x** you would have to assign a *copy* of **x** to **y**, and then modify **y**:

# In[34]:


x = [1,2,3]
y = x.copy()
y.append(4)


# In[35]:


print(x)


# In[36]:


print(y)


# Great! You should now have an understanding of all the methods available for a list in Python!
