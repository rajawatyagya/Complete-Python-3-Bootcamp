#!/usr/bin/env python
# coding: utf-8

# # Chained Comparison Operators
# 
# An interesting feature of Python is the ability to *chain* multiple comparisons to perform a more complex test. You can use these chained comparisons as shorthand for larger Boolean Expressions.
# 
# In this lecture we will learn how to chain comparison operators and we will also introduce two other important statements in Python: **and** and **or**.
# 
# Let's look at a few examples of using chains:

# In[1]:


1 < 2 < 3


# The above statement checks if 1 was less than 2 **and** if 2 was less than 3. We could have written this using an **and** statement in Python:

# In[2]:


1<2 and 2<3


# The **and** is used to make sure two checks have to be true in order for the total check to be true. Let's see another example:

# In[3]:


1 < 3 > 2


# The above checks if 3 is larger than both of the other numbers, so you could use **and** to rewrite it as:

# In[4]:


1<3 and 3>2


# It's important to note that Python is checking both instances of the comparisons. We can also use **or** to write comparisons in Python. For example:

# In[5]:


1==2 or 2<3


# Note how it was true; this is because with the **or** operator, we only need one *or* the other to be true. Let's see one more example to drive this home:

# In[6]:


1==1 or 100==1


# Great! For an overview of this quick lesson: You should have a comfortable understanding of using **and** and **or** statements as well as reading chained comparison code.
# 
# Go ahead and go to the quiz for this section to check your understanding!
