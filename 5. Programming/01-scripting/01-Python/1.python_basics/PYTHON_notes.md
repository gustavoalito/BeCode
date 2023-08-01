## Lists

- The remove() function removes a specified value from the list.

Example: 

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

This will remove the item "banana" from the list.

If you want to remove an item by its index, use the **pop()** function instead:

Example: Remove the 2nd item of the list

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

This will remove the 2nd item of the list ("banana").

**NOTE**: If you do not specify the index, the `pop()` method removes the last item.

- The `del` keyword also removes the specified index:

Example: Remove the first item:

thislist = ["apple", "banana", "cherry"]  
del thislist[0]  
print(thislist)

The `del` keyword can also delete the list completely.

thislist = ["apple", "banana", "cherry"]  
del thislist

The `clear()` method empties the list.

The list still remains, but it has no content.

Example: Clear the list content:

thislist = ["apple", "banana", "cherry"]  
thislist.clear()  
print(thislist)

### Loop Through the Index Numbers

You can also loop through the list items by referring to their index number.

Use the `range()` and `len()` functions to create a suitable iterable.

Example: Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]  
for i in range(len(thislist)):  
  print(thislist[i])

### Using a While Loop

You can loop through the list items by using a `while` loop.

Use the `len()` function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

Remember to increase the index by 1 after each iteration.

Example: Print all items, using a `while` loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]  
i = 0  
while i < len(thislist):  
  print(thislist[i])  
  i = i + 1

### Looping Using List Comprehension

List Comprehension offers the shortest syntax for looping through lists:

Example: A short hand `for` loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]  
[print(x) for x in thislist]

### List Comprehension

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example: Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a `for` statement with a conditional test inside:

Example: 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]  
newlist = []  
  
for x in fruits:  
  if "a" in x:  
    newlist.append(x)  
  
print(newlist)

With list comprehension you can do all that with only one line of code:

Example

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]  
  
newlist = [x for x in fruits if "a" in x]  
  
print(newlist)

#### The Syntax

newlist = [_expression_ for _item_ in _iterable_ if _condition_ == True]

The return value is a new list, leaving the old list unchanged.

---

### Condition

The _condition_ is like a filter that only accepts the items that valuate to `True`.

Example: Only accept items that are not "apple":

newlist = [x for x in fruits if x != "apple"]

The condition if x != "apple"  will return `True` for all elements other than "apple", making the new list contain all fruits except "apple".

The _condition_ is optional and can be omitted:

Example: With no `if` statement:

newlist = [x for x in fruits]


---

### Iterable

The _iterable_ can be any iterable object, like a list, tuple, set etc.

Example: You can use the `range()` function to create an iterable:

newlist = [x for x in range(10)]

Same example, but with a condition:

Example: Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]

---

### Expression

The _expression_ is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

Example: Set the values in the new list to upper case:

newlist = [x.upper() for x in fruits]

You can set the outcome to whatever you like:

Example: Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]

The _expression_ can also contain conditions, not like a filter, but as a way to manipulate the outcome:

Example: Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]

The _expression_ in the example above says:

_"Return the item if it is not banana, if it is banana return orange"._

### Sort Descending

To sort descending, use the keyword argument `reverse = True`

Example: Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]  
thislist.sort(reverse = True)  
print(thislist)

#### Case Insensitive Sort

if you want a case-insensitive sort function, use str.lower as a key function:

Example: Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]  
thislist.sort(key = str.lower)  
print(thislist)

- The **sort()** method sorts the list alphabetically or numerically. It is case sensitive.
- The **reverse()** method reverses the list order., regardless of the alphabet.
- The **copy()** method allows you to copy a list.

thislist = ["apple", "banana", "cherry"]  
mylist = thislist.copy()  
print(mylist)

- You can also copy a list by creating a new list, using the **list()** method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
prinit(mylist)

- Joining 2 lists can be achieved with the **extend()** method. 
list1 = ["a", "b" , "c"]  
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)


## List Methods

Python has a set of built-in methods that you can use on lists.

|Method|Description|
|---|---|
|[append()](https://www.w3schools.com/python/ref_list_append.asp)|Adds an element at the end of the list|
|[clear()](https://www.w3schools.com/python/ref_list_clear.asp)|Removes all the elements from the list|
|[copy()](https://www.w3schools.com/python/ref_list_copy.asp)|Returns a copy of the list|
|[count()](https://www.w3schools.com/python/ref_list_count.asp)|Returns the number of elements with the specified value|
|[extend()](https://www.w3schools.com/python/ref_list_extend.asp)|Add the elements of a list (or any iterable), to the end of the current list|
|[index()](https://www.w3schools.com/python/ref_list_index.asp)|Returns the index of the first element with the specified value|
|[insert()](https://www.w3schools.com/python/ref_list_insert.asp)|Adds an element at the specified position|
|[pop()](https://www.w3schools.com/python/ref_list_pop.asp)|Removes the element at the specified position|
|[remove()](https://www.w3schools.com/python/ref_list_remove.asp)|Removes the item with the specified value|
|[reverse()](https://www.w3schools.com/python/ref_list_reverse.asp)|Reverses the order of the list|
|[sort()](https://www.w3schools.com/python/ref_list_sort.asp)|Sorts the list|

## Tuples

You can create a tuple with only one item. To do so, you need to add a comma after the item, otherwise Python will not recognize it as a tuple.

Example: One item tuple, remember the comma:

thistuple = ("apple",)  
print(type(thistuple))  
  
#NOT a tuple  
thistuple = ("apple")  
print(type(thistuple))

### Construction a Tuple

It is also possible to use the tuple() constructor to make a tuple.

Example: Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets  
print(thistuple)

- The `del` keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")  
del thistuple  
print(thistuple) #this will raise an error because the tuple no longer exists

- The workaround to change of append a tuple is to convert it into a list, do the desired change and then convert it back to a tuple:
thistuple = ("apple", "banana", "cherry")  
y = list(thistuple)  
y.remove("apple")  
thistuple = tuple(y)

You can, however, add a tuple to another tuple:

thistuple = ("apple", "banana", "cherry")  
y = ("orange",)  
thistuple += y  
  
print(thistuple)

## Tuple Methods

Python has two built-in methods that you can use on tuples.

|Method|Description|
|---|---|
|[count()](https://www.w3schools.com/python/ref_tuple_count.asp)|Returns the number of times a specified value occurs in a tuple|
|[index()](https://www.w3schools.com/python/ref_tuple_index.asp)|Searches the tuple for a specified value and returns the position of where it was found|

## Set Methods

Python has a set of built-in methods that you can use on sets.

|Method|Description|
|---|---|
|[add()](https://www.w3schools.com/python/ref_set_add.asp)|Adds an element to the set|
|[clear()](https://www.w3schools.com/python/ref_set_clear.asp)|Removes all the elements from the set|
|[copy()](https://www.w3schools.com/python/ref_set_copy.asp)|Returns a copy of the set|
|[difference()](https://www.w3schools.com/python/ref_set_difference.asp)|Returns a set containing the difference between two or more sets|
|[difference_update()](https://www.w3schools.com/python/ref_set_difference_update.asp)|Removes the items in this set that are also included in another, specified set|
|[discard()](https://www.w3schools.com/python/ref_set_discard.asp)|Remove the specified item|
|[intersection()](https://www.w3schools.com/python/ref_set_intersection.asp)|Returns a set, that is the intersection of two other sets|
|[intersection_update()](https://www.w3schools.com/python/ref_set_intersection_update.asp)|Removes the items in this set that are not present in other, specified set(s)|
|[isdisjoint()](https://www.w3schools.com/python/ref_set_isdisjoint.asp)|Returns whether two sets have a intersection or not|
|[issubset()](https://www.w3schools.com/python/ref_set_issubset.asp)|Returns whether another set contains this set or not|
|[issuperset()](https://www.w3schools.com/python/ref_set_issuperset.asp)|Returns whether this set contains another set or not|
|[pop()](https://www.w3schools.com/python/ref_set_pop.asp)|Removes an element from the set|
|[remove()](https://www.w3schools.com/python/ref_set_remove.asp)|Removes the specified element|
|[symmetric_difference()](https://www.w3schools.com/python/ref_set_symmetric_difference.asp)|Returns a set with the symmetric differences of two sets|
|[symmetric_difference_update()](https://www.w3schools.com/python/ref_set_symmetric_difference_update.asp)|inserts the symmetric differences from this set and another|
|[union()](https://www.w3schools.com/python/ref_set_union.asp)|Return a set containing the union of sets|
|[update()](https://www.w3schools.com/python/ref_set_update.asp)|Update the set with the union of this set and others|

## Dictionaries

### The dict() Constructor

It is also possible to use the dict() constructor to make a dictionary.

Example: Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")  
print(thisdict)

### Accessing Items

You can access the items of a dictionary by referring to its key name, inside square brackets:

Example: Get the value of the "model" key:

thisdict = {  
  "brand": "Ford",  
  "model": "Mustang",  
  "year": 1964  
}  
x = thisdict["model"]

There is also a method called `get()` that will give you the same result:

Example: Get the value of the "model" key:

x = thisdict.get("model")

### Get Keys

The `keys()` method will return a list of all the keys in the dictionary.

Example: Get a list of the keys:

x = thisdict.keys()

### Get Values

The `values()` method will return a list of all the values in the dictionary.

Example: Get a list of the values:

x = thisdict.values()

### Get Items

The `items()` method will return each item in a dictionary, as tuples in a list.

Example: Get a list of the key:value pairs

x = thisdict.items()

### Change Values

You can change the value of a specific item by referring to its key name:

Example: Change the "year" to 2018:

thisdict = {  
  "brand": "Ford",  
  "model": "Mustang",  
  "year": 1964  
}  
thisdict["year"] = 2018

### Update Dictionary

The `update()` method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.

Example: Update the "year" of the car by using the `update()` method:

thisdict = {  
  "brand": "Ford",  
  "model": "Mustang",  
  "year": 1964  
}  
thisdict.update({"year": 2020})

**NOTE:** If the item doesn't exist, then it will be added. Therefore, this is also considered a way of adding a new kay pair into a dictionary.

### Adding Items

Adding an item to the dictionary is done by using a new index key and assigning a value to it:

Example: 

thisdict = {  
  "brand": "Ford",  
  "model": "Mustang",  
  "year": 1964  
}  
thisdict["color"] = "red"  
print(thisdict)

### Looping
- You can use the `values()`, `keys()` or `items()` methods to return values/keys/items of a dictionary:

for x in thisdict.values():  
  print(x)

for x in thisdict.keys():  
  print(x)

for x in thisdict.items():  
  print(x)

## Nested Dictionaries

A dictionary can contain dictionaries, this is called nested dictionaries.

Example: Create a dictionary that contain three dictionaries:

myfamily = {  
  "child1" : {  
    "name" : "Emil",  
    "year" : 2004  
  },  
  "child2" : {  
    "name" : "Tobias",  
    "year" : 2007  
  },  
  "child3" : {  
    "name" : "Linus",  
    "year" : 2011  
  }  
}

Or, if you want to add three dictionaries into a new dictionary:

Example: Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {  
  "name" : "Emil",  
  "year" : 2004  
}  
child2 = {  
  "name" : "Tobias",  
  "year" : 2007  
}  
child3 = {  
  "name" : "Linus",  
  "year" : 2011  
}  
  
myfamily = {  
  "child1" : child1,  
  "child2" : child2,  
  "child3" : child3  
}

### Access Items in Nested Dictionaries

To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

Example: Print the name of child 2:

print(myfamily["child2"]["name"])


## Dictionary Methods

Python has a set of built-in methods that you can use on dictionaries.

|Method|Description|
|---|---|
|[clear()](https://www.w3schools.com/python/ref_dictionary_clear.asp)|Removes all the elements from the dictionary|
|[copy()](https://www.w3schools.com/python/ref_dictionary_copy.asp)|Returns a copy of the dictionary|
|[fromkeys()](https://www.w3schools.com/python/ref_dictionary_fromkeys.asp)|Returns a dictionary with the specified keys and value|
|[get()](https://www.w3schools.com/python/ref_dictionary_get.asp)|Returns the value of the specified key|
|[items()](https://www.w3schools.com/python/ref_dictionary_items.asp)|Returns a list containing a tuple for each key value pair|
|[keys()](https://www.w3schools.com/python/ref_dictionary_keys.asp)|Returns a list containing the dictionary's keys|
|[pop()](https://www.w3schools.com/python/ref_dictionary_pop.asp)|Removes the element with the specified key|
|[popitem()](https://www.w3schools.com/python/ref_dictionary_popitem.asp)|Removes the last inserted key-value pair|
|[setdefault()](https://www.w3schools.com/python/ref_dictionary_setdefault.asp)|Returns the value of the specified key. If the key does not exist: insert the key, with the specified value|
|[update()](https://www.w3schools.com/python/ref_dictionary_update.asp)|Updates the dictionary with the specified key-value pairs|
|[values()](https://www.w3schools.com/python/ref_dictionary_values.asp)|Returns a list of all the values in the dictionary|


## If...Else

### The pass Statement

`if` statements cannot be empty, but if you for some reason have an `if` statement with no content, put in the `pass` statement to avoid getting an error.

Example:

a = 33  
b = 200  
  
if b > a:  
  pass


## While

### The break Statement

With the break statement we can stop the loop even if the while condition is true:

Example:

Exit the loop when i is 3:

i = 1  
while i < 6:  
  print(i)  
  if i == 3:  
    break  
  i += 1

### The continue Statement

With the continue statement we can stop the current iteration, and continue with the next:

Example

Continue to the next iteration if i is 3:

i = 0  
while i < 6:  
  i += 1  
  if i == 3:  
    continue  
  print(i)

## Loops

### The break Statement

With the break statement we can stop the loop before it has looped through all the items:

Example

Exit the loop when `x` is "banana":

fruits = ["apple", "banana", "cherry"]  
for x in fruits:  
  print(x)  
  if x == "banana":  
    break  

Example

Exit the loop when `x` is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]  
for x in fruits:  
  if x == "banana":  
    break  
  print(x)

### The continue Statement

With the continue statement we can stop the current iteration of the loop, and continue with the next:

Example

Do not print banana:

fruits = ["apple", "banana", "cherry"]  
for x in fruits:  
  if x == "banana":  
    continue  
  print(x)

### The range() Function

To loop through a set of code a specified number of times, we can use the range() function,

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

Example

Using the range() function:

for x in range(6):  
  print(x)

**Note** that range(6) is not the values of 0 to 6, but the values 0 to 5.

The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

Example

Using the start parameter:

for x in range(2, 6):  
  print(x)

The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, **3**):

Example

Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):  
  print(x)

### Else in For Loop

The `else` keyword in a `for` loop specifies a block of code to be executed when the loop is finished:

Example

Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):  
  print(x)  
else:  
  print("Finally finished!")

**Note:** The `else` block will NOT be executed if the loop is stopped by a `break` statement.

Example

Break the loop when `x` is 3, and see what happens with the `else` block:

for x in range(6):  
  if x == 3: break  
  print(x)  
else:  
  print("Finally finished!")

### Nested Loops

A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":

Example

Print each adjective for every fruit:

adj = ["red", "big", "tasty"]  
fruits = ["apple", "banana", "cherry"]  
  
for x in adj:  
  for y in fruits:  
    print(x, y)

### The pass Statement

`for` loops cannot be empty, but if you for some reason have a `for` loop with no content, put in the `pass` statement to avoid getting an error.

Example

for x in [0, 1, 2]:  
  pass