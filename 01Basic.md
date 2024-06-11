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

<img src="../src_img/python-list-index.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />
<br />

**try:**
```
My_List = [3, 4, 6, 10]
print(My_List[0])
print(My_List[1])
print(My_List[2])
```
```
My_List.append(8)
print(My_List)
```

```
# prints out 8, 4, 6, 10, 8
for x in My_List:
    print(x)
```
```
mylist = [1,2,3]
print(mylist[10])

# IndexError: list index out of range
```
### Exercise
In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. You must add the number 9 to the "numbers" list, and the word 'Architects' to the "strings" list. \
The result must be **"I love Architects49 more than you"**
```
numbers = [1,2,3]
strings = ['Shma', 'you', 'Design103']

# Hint
numbers.append(...)
strings.append(...)
print("I love " + strings[...] + str(numbers[...])  + str(numbers[...]) + " more than" + strings[...])
```

<img src="../src_img/list2.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />
<br />
---

## Basic Operators
### Arithmetic Operators
 **The addition, subtraction, multiplication, and division** operators can be used with numbers.

```
number = 1 + 2 * 3 / 4.0
print(number)
```
Another operator available is the **modulo (%)** operator, which returns the integer remainder of the division. dividend % divisor = remainder.
```
remainder = 11 % 3
print(remainder)
```
Using **two multiplication symbols** makes a power relationship.
```
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)
```
### Using Operators with Strings
Concatenating **strings** using the **addition operator**
```
helloworld = "hello" + " " + "world"
print(helloworld)
```

### Using Operators with Lists
**Lists** can be joined with the **addition operators**
```
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
```
Just as in **strings**, Python supports forming new **lists** with a repeating sequence using the **multiplication operator**
```
print([1,2,3] * 3)
```
---

## String Formatting
Python uses C-style string formatting to create new, formatted strings. The **"%"** operator is used to format a set of variables enclosed in a **"tuple"** (a fixed size list), together with a format string, which contains normal text together with **"argument specifiers"**, special symbols like **"%s"** and **"%d"**.
```
name = "John"
print("Hello, %s!" % name)
```
To use two or more argument specifiers, use a tuple (parentheses):
```
name = "John"
age = 23
print("%s is %d years old." % (name, age))
```
Any object which is not a string can be formatted using the %s operator as well. The string which returns from the "repr" method of that object is formatted as the string.
```
mylist = [1,2,3]
print("A list: %s" % mylist)
```

**Here are some basic argument specifiers you should know:**

* **%s**
String (or any object with a string representation, like numbers)
* **%d**
Integers
* **%f**
Floating point numbers
* **%.<*number of digits*>f**
Floating point numbers with a fixed amount of digits to the right of the dot.
* **%x/%X**
Integers in hex representation (lowercase/uppercase)

<img src="../src_img/int_hex.png"
     alt="Markdown Monster icon"
     style="margin-right: 0px" />

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