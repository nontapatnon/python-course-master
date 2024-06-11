---
layout: page
title: 01 Basics
---

* [Hello, World!](#hello-world)
* [Variables and Types](#variables-and-types)
* [Lists](#lists)
* [Basic Operators](#basic-operators)
* [String Formatting](#string-formatting)
* [Conditions](#conditions)
* [Loops](#loops)
* [Functions](#functions)
* [Classes and Objects](#classes-and-objects)
* [Dictionaries](#dictionaries)
* [Modules and Packages](#modules-and-packages)

## Hello World
Python is a very simple language, and has a very straightforward syntax. The simplest directive in Python is the "print" directive - it simply prints out a line. 

**Python**
```
print("Hello, World!")
```

**Java**
```
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

**C**
```
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

**C++**
```
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### Indentation
Python uses indentation for blocks, instead of curly braces. Both tabs and spaces are supported, but the standard indentation requires standard Python code to use four spaces.
```
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")
```
---

## Variables and Types

Python is completely object oriented, and not "statically typed". You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.

### Numbers
Python supports two types of numbers:
* integers(whole numbers)
* floating point numbers(decimals).

```
myint = 7
print(myint)
print(type(myint))
```
**and**
```
myfloat = 7.0
print(myfloat)
print(type(myfloat))

myfloat = float(7)
print(myfloat)
print(type(myfloat))
```

### Strings
Strings are defined either with a single quote or a double quotes.

```
myint = 7
print(myint)
print(type(myint))
```
There are additional variations on defining strings that make it easier to include things such as carriage returns, backslashes and Unicode characters.

```
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
```

Assignments can be done on more than one variable "simultaneously" on the same line
```
a, b = 3, 4
print(a, b)
```

Mixing operators
```
one = 1
two = 2
hello = "hello"
print(one + two + hello)
```
---

## Lists
Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner.
<br>
<img src="../src_img/python-list-index.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />
<br>

```
mylist = []
mylist.append(3)
mylist.append(4)
mylist.append(6)
mylist.append(10)
mylist.append(8)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3
```

```
# prints out 1,2,3
for x in mylist:
    print(x)
```
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
## Basic Operators
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
## String Formatting
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
## Conditions
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
## Loops
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
## Functions
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
## Classes and Objects
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
## Dictionaries
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
## Modules and Packages