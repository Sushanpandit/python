Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,4,5,6]
>>> l.count()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    l.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> l.insert(1,2)
>>> l
[1, 2, 2, 3, 4, 5, 6]
>>> l.count(4)
1
>>> l.remove(3)
>>> l
[1, 2, 2, 4, 5, 6]
>>> l.append(2)
>>> l
[1, 2, 2, 4, 5, 6, 2]
>>> l.pop(4)
5
>>> l.pop()
2
>>> l[0]
1
>>> l[0]="apple"
>>> l
['apple', 2, 2, 4, 6]
>>> l[3]="asdfhdgfbju"
>>> l[2]="9"
>>> l
['apple', 2, '9', 'asdfhdgfbju', 6]
>>> l.append(["cow","grapes",6,9})
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> l.append(["cow","grapes",6,9])
>>> l
['apple', 2, '9', 'asdfhdgfbju', 6, ['cow', 'grapes', 6, 9]]
>>> dir(l)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
l.index(cow)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    l.index(cow)
NameError: name 'cow' is not defined. Did you mean: 'pow'?
l.ndex("cow")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    l.ndex("cow")
AttributeError: 'list' object has no attribute 'ndex'. Did you mean: 'index'?
l.index("cow")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    l.index("cow")
ValueError: 'cow' is not in list
l.index(6)
4
l.index(4)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    l.index(4)
ValueError: 4 is not in list
l[5]
['cow', 'grapes', 6, 9]
l[5][6]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    l[5][6]
IndexError: list index out of range
l[5][1]
'grapes'
l[5][4]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    l[5][4]
IndexError: list index out of range
l[5][3]
9
l[5][1]=orange
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    l[5][1]=orange
NameError: name 'orange' is not defined. Did you mean: 'range'?
l[5][1]="orange"
l
['apple', 2, '9', 'asdfhdgfbju', 6, ['cow', 'orange', 6, 9]]
l.append(6,8,"jgyeb","gfhyt")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    l.append(6,8,"jgyeb","gfhyt")
TypeError: list.append() takes exactly one argument (4 given)
")l.append(6,8)
SyntaxError: unterminated string literal (detected at line 1)
l.append(6,8)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    l.append(6,8)
TypeError: list.append() takes exactly one argument (2 given)
l.append(6)
l
['apple', 2, '9', 'asdfhdgfbju', 6, ['cow', 'orange', 6, 9], 6]
l.append("uriybhtyrhguy")
l
['apple', 2, '9', 'asdfhdgfbju', 6, ['cow', 'orange', 6, 9], 6, 'uriybhtyrhguy']
l[5]append.append("kjghbtdgsrkit")
SyntaxError: invalid syntax
