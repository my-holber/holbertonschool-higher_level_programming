# Python3: Mutable, Immutable... Everything is Object!

![Python Objects](data:image/png;base64,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)

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