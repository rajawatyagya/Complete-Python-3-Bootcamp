#!/usr/bin/env python
# coding: utf-8

# # Advanced Strings
# String objects have a variety of methods we can use to save time and add functionality. Let's explore some of them in this lecture:

# In[1]:


s = 'hello world'


# ## Changing case
# We can use methods to capitalize the first word of a string, or change the case of the entire string.

# In[2]:


# Capitalize first word in string
s.capitalize()


# In[3]:


s.upper()


# In[4]:


s.lower()


# Remember, strings are immutable. None of the above methods change the string in place, they only return modified copies of the original string.

# In[5]:


s


# To change a string requires reassignment:

# In[6]:


s = s.upper()
s


# In[7]:


s = s.lower()
s


# ## Location and Counting

# In[9]:


s.count('o') # returns the number of occurrences, without overlap


# In[10]:


s.find('o') # returns the starting index position of the first occurence


# ## Formatting
# The <code>center()</code> method allows you to place your string 'centered' between a provided string with a certain length. Personally, I've never actually used this in code as it seems pretty esoteric...

# In[11]:


s.center(20,'z')


# The <code>expandtabs()</code> method will expand tab notations <code>\t</code> into spaces:

# In[12]:


'hello\thi'.expandtabs()


# ## is check methods
# These various methods below check if the string is some case. Let's explore them:

# In[13]:


s = 'hello'


# <code>isalnum()</code> will return True if all characters in **s** are alphanumeric

# In[14]:


s.isalnum()


# <code>isalpha()</code> will return True if all characters in **s** are alphabetic

# In[15]:


s.isalpha()


# <code>islower()</code> will return True if all cased characters in **s** are lowercase and there is
# at least one cased character in **s**, False otherwise.

# In[16]:


s.islower()


# <code>isspace()</code> will return True if all characters in **s** are whitespace.

# In[17]:


s.isspace()


# <code>istitle()</code> will return True if **s** is a title cased string and there is at least one character in **s**, i.e. uppercase characters may only follow uncased characters and lowercase characters only cased ones. It returns False otherwise.

# In[18]:


s.istitle()


# <code>isupper()</code> will return True if all cased characters in **s** are uppercase and there is
# at least one cased character in **s**, False otherwise.

# In[19]:


s.isupper()


# Another method is <code>endswith()</code> which is essentially the same as a boolean check on <code>s[-1]</code>

# In[20]:


s.endswith('o')


# ## Built-in Reg. Expressions
# Strings have some built-in methods that can resemble regular expression operations.
# We can use <code>split()</code> to split the string at a certain element and return a list of the results.
# We can use <code>partition()</code> to return a tuple that includes the first occurrence of the separator sandwiched between the first half and the end half.

# In[21]:


s.split('e')


# In[22]:


s.partition('l')


# Great! You should now feel comfortable using the variety of methods that are built-in string objects!
