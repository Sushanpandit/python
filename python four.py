Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=("apple",3.14,10)

t=("apple",3.14,10)
t[0]
'apple'
t[3]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t[3]
IndexError: tuple index out of range
t[2]
10
a,b,c=t
a
'apple'
b
3.14
c
10
a.upper
<built-in method upper of str object at 0x000001AE69282F30>
a.upper()
'APPLE'
c.upper()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    c.upper()
AttributeError: 'int' object has no attribute 'upper'
a.title
<built-in method title of str object at 0x000001AE69282F30>
a.title()
'Apple'
dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
del-dir(a)
SyntaxError: cannot delete expression
del_t
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    del_t
NameError: name 'del_t' is not defined
del t

t=("apple",3.14,10)
del t

l=
SyntaxError: invalid syntax
t[1]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    t[1]
NameError: name 't' is not defined
>>> l=[14556,1549,458,"ghyt","asdr"]
>>> min(l)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    min(l)
TypeError: '<' not supported between instances of 'str' and 'int'
>>> l.count()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    l.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> l=[14556,1549,458]
>>> min 1
SyntaxError: invalid syntax
>>> min l
SyntaxError: invalid syntax
>>> lllllll1111212
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    lllllll1111212
NameError: name 'lllllll1111212' is not defined
>>> l=[1,2,3,,4,5,6]
SyntaxError: invalid syntax
>>> l=[1,2,3,,4,5,6]
SyntaxError: invalid syntax
>>> l=[1,2,3,4,5,6]
>>> l.count
<built-in method count of list object at 0x000001AE69312BC0>
>>> l.count()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    l.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> l.remove()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    l.remove()
TypeError: list.remove() takes exactly one argument (0 given)
>>> l.remove(4)
>>> 
