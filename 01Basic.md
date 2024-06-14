---
layout: page
title: 01 Basics
---

* [Hello, World!](#>-hello-world)
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

## >Hello World
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

## >Variables and Types

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

## >Lists
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

## >Basic Operators
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

## >String Formatting
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

* **%s** - String (or any object with a string representation, like numbers)
```
test = "a book"
print("This is %s !" % test)
```

* **%d** - Integers
```
test = 19
print("I am %d years old" % test)
```

* **%f** - Floating point numbers
```
test = 190.985
print("I am %d years old" % test)
```

* **%.<*number of digits*>f** - Floating point numbers with a fixed amount of digits to the right of the dot.
```
test = 190.985
print("I am %.2f years old" % test)
```

* **%x, %X** - Integers in hex representation (lowercase/uppercase)
```
test = 15
print("I am %x years old" % test)
print("I am %X years old" % test)
```

<img src="../src_img/int_hex.png"
     alt="Markdown Monster icon"
     style="margin-right: 0px;" />

### Exercise
You will need to write a format string which prints out the data using the following syntax: **Hello John Doe. Your current balance is $53.44.**
```
data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string ... % data)
```
---
## >Conditions
Python uses **boolean logic** to evaluate conditions. The boolean values True and False are returned when an expression is compared or evaluated. 

```
x = 2
print(x == 2)
print(x == 3)
print(x < 3)
```
The variable assignment is done using a single equals operator **"="**, whereas comparison between two variables is done using the double equals operator **"=="**. The "not equals" operator is marked as **"!="**.

### Boolean operators
The **"and"** and **"or"** boolean operators allow building complex boolean expressions.

```
name = "Nonny"
age = 18
if name == "Nonny" and age == 18:
    print("Your name is Nonny, and you are also 18 years old.")

if name == "Nonny" or name == "Lawrence":
    print("Your name is either Nonny or Lawrence.")
```
```
name = "Nonny"
age = 14
if name == "Nonny" and age != 18:
    print("Your name is Nonny, but you are not yet 18 years old.")
```

```
print("Nonny" == "Nonny")
print(18 != 18)
```

### The "in" operator
The "in" operator could be used to check if a specified object exists within an iterable object container.
```
name = "Nonny"
if name in ["Nonny", "Lawrence"]:
    print("Your name is either Nonny or Lawrence.")
```
Python uses indentation to define code blocks, instead of brackets. The standard Python indentation is **4 spaces**, although **tabs** and **any other space size will work**, as long as it is consistent.
<img src="../src_img/indentation.png"
     alt="Markdown Monster icon"
     style="margin-right: 0px;" />

```
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass
```
```
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")
```
### The 'is' operator
Unlike the double equals operator **"=="**, the **"is"** operator does **not match** the values of the variables, but the instances themselves.
```
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

print(x is x) # Prints out True
```
### The "not" operator
Using **"not"** before a boolean expression inverts it.
```
print(not False) # Prints out True
print((not False) == (False)) # Prints out False
```
---

## >Loops
There are two types of loops in Python, **for** and **while**.

### The "for" loop
For loops iterate over a given sequence.
```
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
```
For loops can iterate over a sequence of numbers using the **"range"** function.
```
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)
```

### "while" loops
While loops repeat as long as a certain **boolean condition** is met.
```
# Prints out 0,1,2,3,4

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1
```
### "break" and "continue" statements
**break** is used to exit a for loop or a while loop, whereas **continue** is used to skip the current block, and return to the **"for"** or **"while"** statement.
```
# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
```
### Can we use "else" clause for loops?
We can use **else** for loops. When the loop condition of **"for"** or **"while"** statement **fails** then code part in **"else" is executed**. If a **break** statement **is executed** inside the for loop then the **"else" part is skipped**. Note that the **"else"** part is executed even if there is a **continue statement**.

```
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
```
### Exercise
Loop through and print out all **even numbers** from the numbers list in the same order they are received. Don't print any numbers that come **after 237** in the sequence.

```
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    ...
    ...
```
---

## >Functions
### What are Functions?
Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. Also functions are a key way to define interfaces so programmers can share their code.
<img src="../src_img/function_machine.png"
     alt="Markdown Monster icon"
     style="margin-right: 0px;" />

<img src="../src_img/domain-and-range-of-a-function.png"
     alt="Markdown Monster icon"
     style="margin-right: 0px;" />

```
block_head:
    1st block line
    2nd block line
    ...
```
Where a **block line** is more Python code (even another block), and the **block head** is of the following format: block_keyword **block_name(argument1,argument2, ...)** Block keywords you already know are "if", "for", and "while".

Functions in python are defined using the block keyword **"def"**, followed with the function's name as the block's name. 

```
def my_function():
    print("Hello From My Function!")
```

Functions may also receive arguments (variables passed from the caller to the function).

```
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
```
Functions may return a value to the caller, using the keyword- **'return'**.

```
def sum_two_numbers(a, b):
    return a + b
```

### How do you call functions in Python?
Simply write the function's name followed by **()**, placing any required arguments within the brackets.
```
def my_function():
    print("Hello From My Function!")

my_function()
```

```
def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

my_function_with_args("John Doe", "a great year!")
```

```
def sum_two_numbers(a, b):
    return a + b

x = sum_two_numbers(1,2)
print(x)
```
### Exercise
xxx
```
...
...
...
```
---

## >Classes and Objects

<img src="../src_img/oop1.png"
     alt="Markdown Monster icon"
     style="margin-right: 0px;" />

**Objects** are an **encapsulation of variables and functions** into a single entity. Objects get their variables and functions from classes. **Classes** are essentially a **template to create your objects**.

<img src="../src_img/oop2.png"
     alt="Markdown Monster icon"
     style="margin-right: 0px;" />
     
<img src="../src_img/oop3.png"
     alt="Markdown Monster icon"
     style="margin-right: 0px;" />
     

     
### ค่อนข้างซับซ้อน ขออธิบายเป็นภาษาไทย 555

OOP เป็นวิธีการเขียนโปรแกรมรูปแบบหนึ่ง โดยมองสิ่งต่างๆในระบบเป็นวัตถุ (Object) ชิ้นหนึ่งที่มีหน้าที่และความหมายในตัว โดยวัตถุๆนั้น ก็มี คุณสมบัติ (Attributes) และ พฤติกรรม (Method,Behavior, Functionality) หรือการกระทำของมัน เป็นการมองบนพื้นฐานความเป็นจริงมากขึ้น

<img src="../src_img/oop4.png"
     alt="Markdown Monster icon"
     style="margin-right: 0px;" />

จากตัวอย่างรูปข้างบน
* Object คือ คน(Person) ประกอบไปด้วย 2 ส่วน
    * คุณสมบัติ(Attributes) ประกอบไปด้วย
        * Name
        * Age
        * Gender
        * Occupation
    * พฤติกรรม (Method, Behavior, Functionality) ซึ่งกอบประกอบไปด้วย
        * Walk()
        * Eat()
        * Sleep()
        * Work()

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_name(self):
        print(self.name, "is employee name")

A49_1 = Person("Nonny", 14)
A49_2 = Person("Lawrence", 12)

print(A49_1.name)
print(A49_2.age)

A49_1.display_name()

```

* `Person`  คือ ชื่อ Class (ขึ้นต้นด้วยตัวพิมพ์ใหญ่)
* `__init__()` คือ Method พิเศษเอาไว้ใช้สำหรับเริ่มต้น (Initialize) คลาส
* `display_name()`  คือ Method ในคำสั่งนี้ก็ทำเพียงแค่แสดงผลคำว่า "... is my name"
* `A49_1` และ  `A49_2` คือ Objects
* `A49_1.display_name()`  คือ การเรียกใช้ Method ของ Objects: `A49_1`

### What is`__init__( )` and `self` in Python ?
ในภาษา Python นั้น   `__init__()`  เป็น Method พิเศษ (Special or Dunder Method) หรือที่เรียกว่า Constructor ก็ได้เช่นกัน ซึ่ง  `__init__()`  จะถูกเรียกใช้โดยอัตโนมัติเมื่อมีการสร้างobjects ของคลาสขึ้นมา หรือเรียกได้ว่าจะเป็นส่วนของการเริ่มต้น (initialize) ของ class

<img src="../src_img/init-viz.png"
     alt="Markdown Monster icon"
     style="margin-right: 0px;" />

Method  `__init__()` ใช้พารามิเตอร์ `self` ซึ่งเป็นการอ้างอิงถึงวัตถุที่กำลังสร้าง เพื่อให้สามารถเข้าถึงคุณสมบัติ (Attributes) และเมธอด (Methods) ของวัตถุ โดยพารามิเตอร์ `self`  ต้องเป็นพารามิเตอร์แรกในเมธอดที่กำหนดในคลาส ถึงแม้ว่าใน Python เราสามารถกำหนดพารามิเตอร์เป็นชื่ออะไรก็ได้ที่ไม่ใช่ `self` แต่สุดท้ายแล้วก็คือธรรมเนียมปฏิบัติ (convension) ของภาษาว่าควรต้องใช้ `self` ถึงจะเหมาะสมที่สุด

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

จากตัวอย่างด้านบนของ class `Person` จะเห็นว่าได้มีการประกาศพารามิเตอร์ 3 ตัว (รวม `self` ด้วย) นั่นก็คือ   `self`, `name` และ `age`

### Method 
Method คือฟังก์ชันที่อยู่ภายใน class โดยเมธอดจะเป็นตัวกำหนดการกระทำ (behavior) ของclass ถ้าสังเกตให้ดีจะเห็นว่า method ก็คือฟังก์ชัน ๆ หนึ่ง เพียงแต่ว่าเป็นฟังก์ชันที่อยู่ภายใต้ class นั่นเอง

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_name(self):
        print(self.name, "is employee name")

A49_1 = Person("Nonny", 14)
A49_1.display_name()
```
จากตัวอย่าง `A49_1.display_name()` จะเห็นว่าเราสามารถเข้าถึง **method** ของ **class** ได้

* `A49_1` คือ objects
* `displya_name()` คือ method



### สรุป
**1. Encapsulation (การห่อหุ้มข้อมูล)**
คือ วิธีการในการซ่อนข้อมูลหรือจำกัดการเข้าถึงข้อมูลบางอย่าง โดยหากต้องการเข้าถึงข้อมูลให้เข้าถึงผ่านทาง Methods หรือเราสามารถกำหนดระดับการเข้าถึงได้ ยกตัวอย่างเช่น public , private

<img src="../src_img/oop5.png"
     alt="Markdown Monster icon"
     style="margin-right: 0px;" />

**2. Inheritance (การสืบทอด)**
เป็นหลักการที่ คลาสแม่ (Super Class) สามารถสืบทอด Attributes และ Method ต่างๆ ไปยัง คลาสลูก (Sub Class) ได้ ซึ่ง คลาสลูกจะได้รับทุกอย่างจากคลาสแม่ และสามารถเพิ่มเติม Attributes หรือ Method เฉพาะตัวเข้าไปได้

<img src="../src_img/oop6.png"
     alt="Markdown Monster icon"
     style="margin-right: 0px;" />

**3. Polymorphism (การพ้องรูป)**
เป็นคุณสมบัติที่ว่า วัตถุใหม่ที่เกิดจากวัตถุแม่ชนิดเดียวกัน มีความสามารถเหมือนแม่แต่การผลลัพธ์การทำงานไม่เหมือนกัน โดยมีลักษณะเฉพาะตัว

<img src="../src_img/oop7.png"
     alt="Markdown Monster icon"
     style="margin-right: 0px;" />
     
**4. Abstraction (หลักการนามธรรม)**
คือ การแสดง Attributes และ Method ของ Object เท่าที่จำเป็น เรารู้แค่ว่า Method นี้ทำงานอย่างไรมี input parametes เป็นอย่างไร แต่ไม่จำเป็นที่ต้องรู้ถึงวิธีการทำงาน เช่น เครื่องชงกาแฟ เรารู้แค่ว่า ใส่เม็ดกาแฟ ,ใส่นม ,ใส่น้ำตาล แต่ไม่จำเป็นต้องรู้ว่าใช้น้ำกี่องศาหรือต้องบดกาแฟละเอียดเท่าไร


## >Dictionaries
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
## >Modules and Packages