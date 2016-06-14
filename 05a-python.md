# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists and tuples are similar in that both are sequences of values. The differences are that lists use [] and tuples use (). The major difference is that tuples are immutable, while lists can be updated. Tuples will work as keys in dictionaries because they are immutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are similar in that both are a collection of elements. The difference is that sets are unordered and do not contain duplicates. An example of a list is "list_a = ["Bob", "Joe", "Jack", "Joe"]" and an example of a set is "set_b = set(["Bob", "Joe", "Jack"])".

>> Finding an element in lists can be done by using their indexes because they are ordered. Set are unordered, so you can't find an element in the same way, but they are good for finding common elements between two sets.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> In Python, lambda is a way to build anonymous functions. One use case is for functions that will only be used once to make the code clearer and more concise.

>> Here's an example of using lambda in the key argument to sorted:

```python
# Creates user info tuple and prints sorted by age
user_info = [
    ('Bob', 21, 'Oakland, CA'),
    ('Joe', 29, 'Alameda, CA'),
    ('Jack', 33, 'Berkeley, CA'),
]
print sorted(user_info, key=lambda info: info[1])
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are an easy and concise way to create lists. Here are examples for list comprehension, map and filter:

```python
# List comprehension
squares_list_comp = [ x**2 for x in range(10) ]
print squares_list_comp

# Map
squares_map = map( lambda x: x**2, range(10) )
print squares_map

# Filter
squares = [ x**2 for x in range(15) ]
squares_filter = filter( lambda x: x <= 81, squares )
print squares_filter
```

>> For specific use cases map() is good for applying a function to every member of an iterable, while filter() is good for returning a list of a sequence that matched the function criteria. List comprehensions are able to accomplish both map() and filter() functionalities.

>> Examples of set comprehensions and dictionary comprehensions:

```python
# Set comprehension
squares_set = set([ x**2 for x in range(10) ])
print squares_set

# Dictionary comprehension
squares_dict = { x: x**2 for x in range(10) }
print squares_dict
```


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> The number of days between the start and stop date for a is 937 days.

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> The number of days between the start and stop date for b is 513 days.

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> The number of days between the start and stop date for c is 7850 days.

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





