#!/usr/bin/env python
# coding: utf-8

# # Advanced Sets
# In this lecture we will learn about the various methods for sets that you may not have seen yet. We'll go over the basic ones you already know and then dive a little deeper.

# In[1]:


s = set()


# # add
# add elements to a set. Remember, a set won't duplicate elements; it will only present them once (that's why it's called a set!)

# In[2]:


s.add(1)


# In[3]:


s.add(2)


# In[4]:


s


# ## clear
# removes all elements from the set

# In[5]:


s.clear()


# In[6]:


s


# ## copy
# returns a copy of the set. Note it is a copy, so changes to the original don't effect the copy.

# In[7]:


s = {1,2,3}
sc = s.copy()


# In[8]:


sc


# In[9]:


s


# In[10]:


s.add(4)


# In[11]:


s


# In[12]:


sc


# ## difference
# difference returns the difference of two or more sets. The syntax is:
# 
#     set1.difference(set2)
# For example:

# In[13]:


s.difference(sc)


# ## difference_update
# difference_update syntax is:
# 
#     set1.difference_update(set2)
# the method returns set1 after removing elements found in set2

# In[14]:


s1 = {1,2,3}


# In[15]:


s2 = {1,4,5}


# In[16]:


s1.difference_update(s2)


# In[17]:


s1


# ## discard
# Removes an element from a set if it is a member. If the element is not a member, do nothing.

# In[18]:


s


# In[19]:


s.discard(2)


# In[20]:


s


# ## intersection and intersection_update
# Returns the intersection of two or more sets as a new set.(i.e. elements that are common to all of the sets.)

# In[21]:


s1 = {1,2,3}


# In[22]:


s2 = {1,2,4}


# In[23]:


s1.intersection(s2)


# In[24]:


s1


# intersection_update will update a set with the intersection of itself and another.

# In[25]:


s1.intersection_update(s2)


# In[26]:


s1


# ## isdisjoint
# This method will return True if two sets have a null intersection.

# In[27]:


s1 = {1,2}
s2 = {1,2,4}
s3 = {5}


# In[28]:


s1.isdisjoint(s2)


# In[29]:


s1.isdisjoint(s3)


# ## issubset
# This method reports whether another set contains this set.

# In[30]:


s1


# In[31]:


s2


# In[32]:


s1.issubset(s2)


# ## issuperset
# This method will report whether this set contains another set.

# In[33]:


s2.issuperset(s1)


# In[34]:


s1.issuperset(s2)


# ## symmetric_difference and symmetric_update
# Return the symmetric difference of two sets as a new set.(i.e. all elements that are in exactly one of the sets.)

# In[35]:


s1


# In[36]:


s2


# In[37]:


s1.symmetric_difference(s2)


# ## union
# Returns the union of two sets (i.e. all elements that are in either set.)

# In[38]:


s1.union(s2)


# ## update
# Update a set with the union of itself and others.

# In[39]:


s1.update(s2)


# In[40]:


s1


# Great! You should now have a complete awareness of all the methods available to you for a set object type. This data structure is extremely useful and is underutilized by beginners, so try to keep it in mind!
# 
# Good Job!
