Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("\nDict CUBES : ",{x: x**3 for x in range(10)})

Dict CUBES :  {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
print("Dict CUBES EVEN: ",{x: x**3 for x in range(10) if x**3 % 2 == 0})
Dict CUBES EVEN:  {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}
l=list(range(1,100,4))
for key,value in enumerate(l):
    print(key," :: ",value)

    
0  ::  1
1  ::  5
2  ::  9
3  ::  13
4  ::  17
5  ::  21
6  ::  25
7  ::  29
8  ::  33
9  ::  37
10  ::  41
11  ::  45
12  ::  49
13  ::  53
14  ::  57
15  ::  61
16  ::  65
17  ::  69
18  ::  73
19  ::  77
20  ::  81
21  ::  85
22  ::  89
23  ::  93
24  ::  97
for key,value in enumerate(l):
    print(key," :: ",value)

    
0  ::  1
1  ::  5
2  ::  9
3  ::  13
4  ::  17
5  ::  21
6  ::  25
7  ::  29
8  ::  33
9  ::  37
10  ::  41
11  ::  45
12  ::  49
13  ::  53
14  ::  57
15  ::  61
16  ::  65
17  ::  69
18  ::  73
19  ::  77
20  ::  81
21  ::  85
22  ::  89
23  ::  93
24  ::  97
l=list(range(1,500,4))
for key,value in enumerate(l):
    print(key," :: ",value)
    
SyntaxError: multiple statements found while compiling a single statement
l=list(range(1,500,4))
for key,value in enumerate(l):
    print(key," :: ",value)
    
SyntaxError: multiple statements found while compiling a single statement
l=list(range(1,100,4))
for key,value in enumerate(l):
    print(key," :: ",value)

    
0  ::  1
1  ::  5
2  ::  9
3  ::  13
4  ::  17
5  ::  21
6  ::  25
7  ::  29
8  ::  33
9  ::  37
10  ::  41
11  ::  45
12  ::  49
13  ::  53
14  ::  57
15  ::  61
16  ::  65
17  ::  69
18  ::  73
19  ::  77
20  ::  81
21  ::  85
22  ::  89
23  ::  93
24  ::  97
>>> print([str(i) for i in range(10)])
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> KeyboardInterrupt
>>> print([str(i) for i in range(10)])
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> print for i in range(10)])
SyntaxError: unmatched ']'
>>> print([(i) for i in range(10)])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> i = map(str,range(10)) #2
>>> print(list(i))
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> print(list(i))
[]
>>> i = map(range(10,100,2)) #2
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    i = map(range(10,100,2)) #2
TypeError: map() must have at least two arguments.
>>> i = map(range(10,100,2)) #2
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    i = map(range(10,100,2)) #2
TypeError: map() must have at least two arguments.
