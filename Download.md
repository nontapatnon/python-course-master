---
layout: page
title: Download
---


<!-- * For Python script in class [Download](https://nontapatnon.github.io/python-course-master/Teaching/python.py) -->

<!-- * For Python script in class [This](https://nontapatnon.github.io/python-course-master/Teaching/python.py 'Link title')

* For Python script in class [This](https://nontapatnon.github.io/python-course-master/Teaching/python.txt 'Link title') -->


### For the Python script in this class (July 2024) is below:

```
class Box:

    # shared variable for all object create by this class
    color = 'green'

    # class method for object
    def __init__(self, width, height, dept):
        self.width = width
        self.height = height
        self.dept = dept

     # class method for object
    def getVolume(self):
        return self.width * self.height * self.dept

    @staticmethod
    def compare(a, b):
        if a.getVolume() > b.getVolume():
            return 'greater than'
        elif a.getVolume() == b.getVolume():
            return 'equal'
        else:
            return 'less than'

a = Box(2, 3, 4)
b = Box(1, 2, 5)

Box.color = 'red'

print('Box a volume = %d' % a.getVolume())
print('Box b volume = %d' % b.getVolume())

print('Box a color = %s' % a.color)
print('Box b color = %s' % b.color)

print('Box a volume a is %s box b' % Box.compare(a, b))



```