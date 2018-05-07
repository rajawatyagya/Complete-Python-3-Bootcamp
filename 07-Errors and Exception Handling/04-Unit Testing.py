#!/usr/bin/env python
# coding: utf-8

# # Unit Testing
# 
# Equally important as writing good code is writing good tests. Better to find bugs yourself than have them reported to you by end users!
# 
# For this section we'll be working with files outside the notebook. We'll save our code to a .py file, and then save our test script to another .py file. Normally we would code these files using a text editor like Brackets or Atom, or inside an IDE like Spyder or Pycharm. But, since we're here, let's use Jupyter!
# 
# Recall that with some IPython magic we can write the contents of a cell to a file using `%%writefile`.<br>
# Something we haven't seen yet; you can run terminal commands from a jupyter cell using `!`
# 
# ## Testing tools
# 
# There are dozens of good testing libraries out there. Most are third-party packages that require an install, such as:
# 
# * [pylint](https://www.pylint.org/)
# * [pyflakes](https://pypi.python.org/pypi/pyflakes/)
# * [pep8](https://pypi.python.org/pypi/pep8)
# 
# These are simple tools that merely look at your code, and they'll tell you if there are style issues or simple problems like variable names being called before assignment.
# 
# A far better way to test your code is to write tests that send sample data to your program, and compare what's returned to a desired outcome.<br>Two such tools are available from the standard library:
# 
# * [unittest](https://docs.python.org/3/library/unittest.html)
# * [doctest](https://docs.python.org/3/library/doctest.html)
# 
# Let's look at pylint first, then we'll do some heavier lifting with unittest.
# 

# ## `pylint`
# 
# `pylint` tests for style as well as some very basic program logic.

# First, if you don't have it already (and you probably do, as it's part of the Anaconda distribution), you should install `pylint`.<br>Once that's done feel free to comment out the cell, you won't need it anymore.

# In[ ]:


get_ipython().system(' pip install pylint')


# Let's save a very simple script:

# In[1]:


get_ipython().run_cell_magic('writefile', 'simple1.py', 'a = 1\nb = 2\nprint(a)\nprint(B)')


# Now let's check it using pylint

# In[2]:


get_ipython().system(' pylint simple1.py')


# Pylint first lists some styling issues - it would like to see an extra newline at the end, modules and function definitions should have descriptive docstrings, and single characters are a poor choice for variable names.
# 
# More importantly, however, pylint identified an error in the program - a variable called before assignment. This needs fixing.
# 
# Note that pylint scored our program a negative 12.5 out of 10. Let's try to improve that!

# In[3]:


get_ipython().run_cell_magic('writefile', 'simple1.py', '"""\nA very simple script.\n"""\n\ndef myfunc():\n    """\n    An extremely simple function.\n    """\n    first = 1\n    second = 2\n    print(first)\n    print(second)\n\nmyfunc()')


# In[4]:


get_ipython().system(' pylint simple1.py')


# Much better! Our score climbed to 8.33 out of 10. Unfortunately, the final newline has to do with how jupyter writes to a file, and there's not much we can do about that here. Still, pylint helped us troubleshoot some of our problems. But what if the problem was more complex?

# In[5]:


get_ipython().run_cell_magic('writefile', 'simple2.py', '"""\nA very simple script.\n"""\n\ndef myfunc():\n    """\n    An extremely simple function.\n    """\n    first = 1\n    second = 2\n    print(first)\n    print(\'second\')\n\nmyfunc()')


# In[6]:


get_ipython().system(' pylint simple2.py')


# pylint tells us there's an unused variable in line 10, but it doesn't know that we might get an unexpected output from line 12! For this we need a more robust set of tools. That's where `unittest` comes in.

# ## `unittest`
# `unittest` lets you write your own test programs. The goal is to send a specific set of data to your program, and analyze the returned results against an expected result. 
# 
# Let's generate a simple script that capitalizes words in a given string. We'll call it **cap.py**.

# In[7]:


get_ipython().run_cell_magic('writefile', 'cap.py', 'def cap_text(text):\n    return text.capitalize()')


# Now we'll write a test script. We can call it whatever we want, but **test_cap.py** seems an obvious choice.
# 
# When writing test functions, it's best to go from simple to complex, as each function will be run in order. Here we'll test simple, one-word strings, followed by a test of multiple word strings.

# In[8]:


get_ipython().run_cell_magic('writefile', 'test_cap.py', "import unittest\nimport cap\n\nclass TestCap(unittest.TestCase):\n    \n    def test_one_word(self):\n        text = 'python'\n        result = cap.cap_text(text)\n        self.assertEqual(result, 'Python')\n        \n    def test_multiple_words(self):\n        text = 'monty python'\n        result = cap.cap_text(text)\n        self.assertEqual(result, 'Monty Python')\n        \nif __name__ == '__main__':\n    unittest.main()")


# In[9]:


get_ipython().system(' python test_cap.py')


# What happened? It turns out that the `.capitalize()` method only capitalizes the first letter of the first word in a string. Doing a little research on string methods, we find that `.title()` might give us what we want.

# In[10]:


get_ipython().run_cell_magic('writefile', 'cap.py', 'def cap_text(text):\n    return text.title()  # replace .capitalize() with .title()')


# In[11]:


get_ipython().system(' python test_cap.py')


# Hey, it passed! But have we tested all cases? Let's add another test to **test_cap.py** to see if it handles words with apostrophes, like *don't*.
# 
# In a text editor this would be easy, but in Jupyter we have to start from scratch.

# In[12]:


get_ipython().run_cell_magic('writefile', 'test_cap.py', 'import unittest\nimport cap\n\nclass TestCap(unittest.TestCase):\n    \n    def test_one_word(self):\n        text = \'python\'\n        result = cap.cap_text(text)\n        self.assertEqual(result, \'Python\')\n        \n    def test_multiple_words(self):\n        text = \'monty python\'\n        result = cap.cap_text(text)\n        self.assertEqual(result, \'Monty Python\')\n        \n    def test_with_apostrophes(self):\n        text = "monty python\'s flying circus"\n        result = cap.cap_text(text)\n        self.assertEqual(result, "Monty Python\'s Flying Circus")\n        \nif __name__ == \'__main__\':\n    unittest.main()')


# In[13]:


get_ipython().system(' python test_cap.py')


# Now we have to find a solution that handles apostrophes! There is one (look up `capwords` from the `string` module) but we'll leave that as an exercise for the reader.

# Great! Now you should have a basic understanding of unit testing!
