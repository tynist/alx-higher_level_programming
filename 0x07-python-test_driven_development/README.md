0x07. Python - Test-driven development
======================================

-   By Guillaume

Concepts
*For this project, we expect you to look at this concept:*

[Never forget a test](https://alx-intranet.hbtn.io/concepts/47)


Background Context
------------------

**Important notice on intranet checks for Python projects**
Starting from today:

Based on the requirements of each task, **you should always write the documentation (module(s) + function(s)) and tests first**, before you actually code anything
The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
We strongly encourage you to work together on test cases, so that you don’t miss any edge case. **But not in the implementation of them!**
**Don’t trust the user**, always think about all possible edge cases


Resources
---------

**Read or watch**:

-   [doctest — Test interactive Python examples](https://alx-intranet.hbtn.io/rltoken/BwZJVq2MQ1_Vg_3gphoitQ) *(until “26.2.3.7. Warnings” included)*
-   [doctest – Testing through documentation](https://alx-intranet.hbtn.io/rltoken/96kLRRIOHzsn3VDDXT21HA)
-   [Unit Tests in Python](https://alx-intranet.hbtn.io/rltoken/wfuUl81Q3Nku1qCzdDHAfA)

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/ER6JIfkhcpsfFWZNN_BBvg "explain to anyone"), **without the help of Google**:

### General

-   Why Python programming is awesome
-   What's the difference between errors and exceptions
-   What are exceptions and how to use them
-   When do we need to use exceptions
-   How to correctly handle an exception
-   What's the purpose of catching exceptions
-   How to raise a builtin exception
-   When do we need to implement a clean-up action after an exception

### Copyright - Plagiarism
-   You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
-   You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
-   You are not allowed to publish any content of this project.
-   Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/python3`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the pycodestyle (version 2.7.*)
-   All your files must be executable
-   The length of your files will be tested using `wc`

### Python Test Cases
-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files should end with a new line
-   All your test files should be inside a folder `tests`
-   All your test files should be text files (extension: `.txt`)
-   All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
-   We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!


Tasks
-----

### 0\. Integers addition
Write a function that adds 2 integers.

-   Prototype: `def add_integer(a, b=98)`:
-   `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer or b must be an integer`
-   `a` and `b` must be first casted to integers if they are float
-   Returns an integer: the addition of `a` and `b`
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x07$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x07$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
guillaume@ubuntu:~/0x07$
```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x07-python-test_driven_development`
-   File: `0-add_integer.py, tests/0-add_integer.txt`

