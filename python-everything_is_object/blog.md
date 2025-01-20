# Python3: Mutable, Immutable... Everything is Object!

![Python Objects](https://media.geeksforgeeks.org/wp-content/uploads/20230605074523/What-is-Python.webp)

## Introduction

In Python, **everything is an object**, from simple integers to complex data structures. Understanding the difference between **mutable** and **immutable** objects is crucial to mastering Python and writing efficient, bug-free code. This post explores object identity, types, mutability, and how Python handles object references and function arguments.

## id and type

In Python, every object has a unique **identity** and a **type**. The identity of an object can be checked using the `id()` function, which returns the object's memory address. The `type()` function tells us what kind of object we are dealing with.

```python
x = 42
y = "hello"
print(id(x), type(x))  # Example output: 140710090244336 <class 'int'>
print(id(y), type(y))  # Example output: 140710090753200 <class 'str'>
```

Objects with the same value might have different identities if they are mutable, while immutable objects might share the same identity if their values are the same (due to interning).

```python
a = 10
b = 10
print(id(a) == id(b))  # True (because integers are immutable and interned)
```

## Mutable Objects

**Mutable objects** are those whose values can be changed after they are created. Common mutable types include:

- Lists (`list`)
- Dictionaries (`dict`)
- Sets (`set`)

Example:

```python
my_list = [1, 2, 3]
print(id(my_list))  # 140292883692160
my_list.append(4)
print(id(my_list))  # 140292883692160 (same ID, modified object)
```

The ID remains the same because we modified the object in place.

## Immutable Objects

**Immutable objects** cannot be changed once created. Common immutable types include:

- Integers (`int`)
- Floats (`float`)
- Strings (`str`)
- Tuples (`tuple`)

Example:

```python
x = "hello"
print(id(x))  # 140710090753200
x = x + " world"
print(id(x))  # 140710090754000 (different ID, new object created)
```

Operations on immutable objects result in the creation of new objects rather than modifying the existing ones.

## Why Does It Matter?

Understanding mutability affects how Python handles objects:

- Mutable objects can lead to **unexpected side effects**, especially when passed to functions.
- Immutable objects ensure **data integrity** and are hashable, making them ideal for dictionary keys and set elements.

Example of unexpected side effects with mutable objects:

```python
def modify_list(lst):
    lst.append(100)

nums = [1, 2, 3]
modify_list(nums)
print(nums)  # [1, 2, 3, 100] (unexpected modification)
```

With immutable objects, such side effects are avoided:

```python
def modify_string(s):
    s = s + " world"

msg = "hello"
modify_string(msg)
print(msg)  # "hello" (original remains unchanged)
```

## Function Arguments and Implications

Python function arguments are passed **by object reference**, meaning:

- If the argument is mutable, changes inside the function affect the original object.
- If the argument is immutable, any modifications inside the function create a new object.

Example with mutable object:

```python
def add_element(lst):
    lst.append(99)

my_list = [1, 2, 3]
add_element(my_list)
print(my_list)  # [1, 2, 3, 99] (mutated)
```

Example with immutable object:

```python
def change_value(num):
    num = 20

x = 10
change_value(x)
print(x)  # 10 (unchanged)
```

## Advanced Insights

Some advanced concepts related to mutability include:

- **Copying:** Using `copy()` or `deepcopy()` to create copies of mutable objects.
- **Interning:** Optimization for small integers and strings.
- **Memory efficiency:** Using tuples instead of lists for fixed data.

Example of deep copy:

```python
import copy
original = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

shallow_copy[0][0] = 99
print(original)  # [[99, 2, 3], [4, 5, 6]] (shallow copy affected)
print(deep_copy) # [[1, 2, 3], [4, 5, 6]] (deep copy remains intact)
```

## Conclusion

Understanding mutable vs. immutable objects is fundamental to writing efficient Python code. It helps in memory optimization, avoiding side effects, and ensuring proper function behavior. Whether working with simple data types or complex structures, knowing when to use mutable vs. immutable objects can greatly impact your program's performance and correctness.

If you found this post helpful, feel free to share it on LinkedIn and leave your thoughts in the comments!

## References
- [Python Official Documentation](https://docs.python.org/3/)
- [Python Memory Management](https://realpython.com/python-memory-management/)
