Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={'a':"apple",'b':"ball",'c':567.2145,'d':78.12}
d['a']
'apple'
d['d']
78.12
dir(d)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
d['e']=gfhy
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d['e']=gfhy
NameError: name 'gfhy' is not defined
d['e']=gfhy
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d['e']=gfhy
NameError: name 'gfhy' is not defined
"
d['e']="gfhy"
d['e']="gfhy"
d
{'a': 'apple', 'b': 'ball', 'c': 567.2145, 'd': 78.12, 'e': 'gfhy'}
d['k']="asdgh"
d
{'a': 'apple', 'b': 'ball', 'c': 567.2145, 'd': 78.12, 'e': 'gfhy', 'k': 'asdgh'}
d[1o]="ten"
SyntaxError: invalid decimal literal
d[10]="ten"
d
{'a': 'apple', 'b': 'ball', 'c': 567.2145, 'd': 78.12, 'e': 'gfhy', 'k': 'asdgh', 10: 'ten'}
d.pop(10)
'ten'
help(d.popitem)
Help on built-in function popitem:

popitem() method of builtins.dict instance
    Remove and return a (key, value) pair as a 2-tuple.
    
    Pairs are returned in LIFO (last-in, first-out) order.
    Raises KeyError if the dict is empty.

for x in d:
    print(x)

    
a
b
c
d
e
k
for x in d:
    print(x,d[x])

    
a apple
b ball
c 567.2145
d 78.12
e gfhy
k asdgh
>>> for x in d:
...     print(x,----d[x])
... 
...     
Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    print(x,----d[x])
TypeError: bad operand type for unary -: 'str'
>>> for x in d:
...     print(x,"----"d[x])
...     
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> for x in d:
...     print(x,"----",d[x])
... 
...     
a ---- apple
b ---- ball
c ---- 567.2145
d ---- 78.12
e ---- gfhy
k ---- asdgh
>>> d=list(s)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    d=list(s)
NameError: name 's' is not defined
>>> s="python programming"
>>> l=list(s)
>>> un=set(s)
>>> un=set(l)
>>> news=list(un)
>>> l
['p', 'y', 't', 'h', 'o', 'n', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
>>> un
{'i', 't', 'a', 'y', 'g', 'm', ' ', 'p', 'r', 'h', 'o', 'n'}
>>> news
['i', 't', 'a', 'y', 'g', 'm', ' ', 'p', 'r', 'h', 'o', 'n']
