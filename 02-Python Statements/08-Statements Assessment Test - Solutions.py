#!/usr/bin/env python
# coding: utf-8

# # Statements Assessment Solutions

# _____
# **Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**

# In[1]:


st = 'Print only the words that start with s in this sentence'


# In[2]:


for word in st.split():
    if word[0] == 's':
        print(word)


# ______
# **Use range() to print all the even numbers from 0 to 10.**

# In[3]:


list(range(0,11,2))


# ___
# **Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**

# In[4]:


[x for x in range(1,51) if x%3 == 0]


# _____
# **Go through the string below and if the length of a word is even print "even!"**

# In[5]:


st = 'Print every word in this sentence that has an even number of letters'


# In[6]:


for word in st.split():
    if len(word)%2 == 0:
        print(word+" <-- has an even length!")


# ____
# **Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**

# In[ ]:


for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# ____
# **Use a List Comprehension to create a list of the first letters of every word in the string below:**

# In[7]:


st = 'Create a list of the first letters of every word in this string'


# In[8]:


[word[0] for word in st.split()]


# ### Great Job!
