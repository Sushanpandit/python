Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x="asdfghjkl"
dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
x.count(" ")
0
x.split
<built-in method split of str object at 0x000002377C41C330>
help(x.split)
Help on built-in function split:

split(sep=None, maxsplit=-1) method of builtins.str instance
    Return a list of the substrings in the string, using sep as the separator string.
    
      sep
        The separator used to split the string.
    
        When set to None (the default value), will split on any whitespace
        character (including \\n \\r \\t \\f and spaces) and will discard
        empty strings from the result.
      maxsplit
        Maximum number of splits (starting from the left).
        -1 (the default value) means no limit.
    
    Note, str.split() is mainly useful for data that has been intentionally
    delimited.  With natural text that includes punctuation, consider using
    the regular expression module.

x.spliy()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x.spliy()
AttributeError: 'str' object has no attribute 'spliy'. Did you mean: 'split'?
x.split( )
['asdfghjkl']
x.split(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x.split(a)
NameError: name 'a' is not defined
#name
#name=sushan
help(x.rjust)
Help on built-in function rjust:

rjust(width, fillchar=' ', /) method of builtins.str instance
    Return a right-justified string of length width.
    
    Padding is done using the specified fill character (default is a space).

name="padding\nis\ndone\nusing\nthe\nspecified"
print(name)
padding
is
done
using
the
specified
name="padding \nis \ndone \nusing \nthe \nspecified"
print(name)
padding 
is 
done 
using 
the 
specified
name="padding \tis \tdone \tusing \tthe \tspecified"
print(name)
padding 	is 	done 	using 	the 	specified
name.count(" ")
5
name.count("\t ")
0
name.count("\t")
5
name.split( )
['padding', 'is', 'done', 'using', 'the', 'specified']
name="as\sfg"
print(name)
as\sfg
name="as \sfg"
print(name)
as \sfg
letters="Padding is done using the specified fill character default is a spaceReturn a right justified string of length width.rjust(width, fillchu7t method of builtins.str instance"
print(name)
as \sfg
print(letters)
Padding is done using the specified fill character default is a spaceReturn a right justified string of length width.rjust(width, fillchu7t method of builtins.str instance
letters="""Padding is done using the specified fill character default is a spaceReturn a right justified string of length width.rjust(width, fillchu7t method of builtins.str instance"""
                                                                                                                           
print(letters)
                                                                                                                           
Padding is done using the specified fill character default is a spaceReturn a right justified string of length width.rjust(width, fillchu7t method of builtins.str instance
ssp="""Padding is done using the specified fill character default is a spaceReturn a right justified string of length width.rjust(width, fillchu7t method of builtins.str instance"""
                                                                                                                           
print(ssp)
                                                                                                                           
Padding is done using the specified fill character default is a spaceReturn a right justified string of length width.rjust(width, fillchu7t method of builtins.str instance
"""Padding is done using the specified fill character default is a spaceReturn a right justified string of length width.rjust(width, fillchu7t method of builtins.str instance"""
                                                                                                                           
'Padding is done using the specified fill character default is a spaceReturn a right justified string of length width.rjust(width, fillchu7t method of builtins.str instance'
dir(letters)
                                                                                                                           
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
help(letters.casefold)
                                                                                                                           
Help on built-in function casefold:

casefold() method of builtins.str instance
    Return a version of the string suitable for caseless comparisons.

age=20
                                                                                                                           
if >:10
                                                                                                                           
SyntaxError: invalid syntax
age=20
                                                                                                                           
if age<30:


                                                                                                                           \
                                                                                                                           [hjhjghmb

                                                                                                                            njmghjfg
KeyboardInterrupt
if age>30:
                                                                                                                
KeyboardInterrupt
if age<30:
                                                                                                                            print("okay")

                                                                                                                            
okay
if if age<30:


                                                                                                                           \
                                                                                                                           [hjhjghmb

                                                                                                                            njmghjfg
                                                                                                                            
SyntaxError: invalid syntax
if age<10:
                                                                                                                            print("okay")

                                                                                                                            
if age<10:
                                                                                                                            print("yes")

                                                                                                                            
a=5
                                                                                                                            
if a==10:
                                                                                                                            print("yes")

                                                                                                                            
a=5
                                                                                                                            
a=5
                                                                                                                            
a=5
                                                                                                                            
if a==10:
                                                                                                                            print("yes")
else:
    print("no")

    
no
a==10
False
a==10|| a<=4
SyntaxError: invalid syntax
a==10| a<=4
False
a==10& a<=8
False
a==10 or a<=4
False
a==10 and a>8
False
a==10 and a==10
False
a==10 or a=10
SyntaxError: cannot assign to expression
a==10 or a<=10
True
a=5
if a==10 and a<=8 and a>20 or a>12:
    print("yes")
else:
    print"(no")
    
SyntaxError: unmatched ')'
if a==10 and a<=8 and a>20 or a>12:
    print("yes")
else:
    print"(no")if a==10 and a<=8 and a>20 or a>12:
        print("yes")
    else:
        print"(no")
        
SyntaxError: unmatched ')'
if a==10 and a<=8 and a>20 or a>12:
    print("yes")
else:
    print("no")

    
no
if a==20 and a>10 and a<=13 or a>=2:
    print("yes")
else:
    print("no")

    
yes
if a==20 and (a>10 and (a<=13 or a>=2)):
    print("yes")
else:
    print("no")


    

    print("yes")
else:
    print("no")
    
SyntaxError: invalid syntax
if a==130 and (a>120 and ( a> 130 or a>=45)):
    print("yes")
else:
    print("no")

    
no
if a==35 and a<=20 or a>=34:
    print("yes")
elif a==24 and a<=3 or a>=12:
    print("ok")
else a==12 and a<=12 or a>=34:
    
SyntaxError: expected ':'
if a==35 and a<=20 or a>=34:
    print("yes")
elif a==24 and a<=3 or a>=12:
    print("ok")
else a==12 and a<=12 or a>=34:
    
SyntaxError: expected ':'
if a==35 and a<=20 or a>=34:
    print("yes")
elif a==24 and a<=3 or a>=12:
    print("ok")
else:
    print("no")

    
no
name="Python"
't' in name
True
for in name:
    
SyntaxError: invalid syntax
name="Python"
't' in name
True
for a in name:
    print("a")

    
a
a
a
a
a
a
name="Python"
't' in name
True
for a in name:
    print(a)

    
P
y
t
h
o
n
name="Python"'t'
't' in name
True
for a in range(10):
    print(a)

    
0
1
2
3
4
5
6
7
8
9
for a in range(1000):
    print(a)

    
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
755
756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
862
863
864
865
866
867
868
869
870
871
872
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
916
917
918
919
920
921
922
923
924
925
926
927
928
929
930
931
932
933
934
935
936
937
938
939
940
941
942
943
944
945
946
947
948
949
950
951
952
953
954
955
956
957
958
959
960
961
962
963
964
965
966
967
968
969
970
971
972
973
974
975
976
977
978
979
980
981
982
983
984
985
986
987
988
989
990
991
992
993
994
995
996
997
998
999
for i in range(100,200):
    if i>250:
        print(i(str)+"250")
    if(i==300):
        print("two hundred")
    if (i>=350):
        print("three hundred")

        

for i in range(100,200):
    if i>250:
        print(i(str)+"250")
    if(i==300):
        print("two hundred")
    if (i>=350):
        print("three hundred")

        
for i in range(100,200):
    if i>250:
        print(i+"250")
    if(i==300):
        print("two hundred")
    if (i>=350):
        print("three hundred")

        
for i in range(100,200):
    if i>250:
        print(str(i)+"250")
    if(i==300):
        print("two hundred")
    if (i>=350):
        print("three hundred")

        
for i in range(100,500):
    if i>250:
        print(str(i)+"250")
    if(i==300):
        print("two hundred")
    if (i>=350):
        print("three hundred")

        
251250
252250
253250
254250
255250
256250
257250
258250
259250
260250
261250
262250
263250
264250
265250
266250
267250
268250
269250
270250
271250
272250
273250
274250
275250
276250
277250
278250
279250
280250
281250
282250
283250
284250
285250
286250
287250
288250
289250
290250
291250
292250
293250
294250
295250
296250
297250
298250
299250
300250
two hundred
301250
302250
303250
304250
305250
306250
307250
308250
309250
310250
311250
312250
313250
314250
315250
316250
317250
318250
319250
320250
321250
322250
323250
324250
325250
326250
327250
328250
329250
330250
331250
332250
333250
334250
335250
336250
337250
338250
339250
340250
341250
342250
343250
344250
345250
346250
347250
348250
349250
350250
three hundred
351250
three hundred
352250
three hundred
353250
three hundred
354250
three hundred
355250
three hundred
356250
three hundred
357250
three hundred
358250
three hundred
359250
three hundred
360250
three hundred
361250
three hundred
362250
three hundred
363250
three hundred
364250
three hundred
365250
three hundred
366250
three hundred
367250
three hundred
368250
three hundred
369250
three hundred
370250
three hundred
371250
three hundred
372250
three hundred
373250
three hundred
374250
three hundred
375250
three hundred
376250
three hundred
377250
three hundred
378250
three hundred
379250
three hundred
380250
three hundred
381250
three hundred
382250
three hundred
383250
three hundred
384250
three hundred
385250
three hundred
386250
three hundred
387250
three hundred
388250
three hundred
389250
three hundred
390250
three hundred
391250
three hundred
392250
three hundred
393250
three hundred
394250
three hundred
395250
three hundred
396250
three hundred
397250
three hundred
398250
three hundred
399250
three hundred
400250
three hundred
401250
three hundred
402250
three hundred
403250
three hundred
404250
three hundred
405250
three hundred
406250
three hundred
407250
three hundred
408250
three hundred
409250
three hundred
410250
three hundred
411250
three hundred
412250
three hundred
413250
three hundred
414250
three hundred
415250
three hundred
416250
three hundred
417250
three hundred
418250
three hundred
419250
three hundred
420250
three hundred
421250
three hundred
422250
three hundred
423250
three hundred
424250
three hundred
425250
three hundred
426250
three hundred
427250
three hundred
428250
three hundred
429250
three hundred
430250
three hundred
431250
three hundred
432250
three hundred
433250
three hundred
434250
three hundred
435250
three hundred
436250
three hundred
437250
three hundred
438250
three hundred
439250
three hundred
440250
three hundred
441250
three hundred
442250
three hundred
443250
three hundred
444250
three hundred
445250
three hundred
446250
three hundred
447250
three hundred
448250
three hundred
449250
three hundred
450250
three hundred
451250
three hundred
452250
three hundred
453250
three hundred
454250
three hundred
455250
three hundred
456250
three hundred
457250
three hundred
458250
three hundred
459250
three hundred
460250
three hundred
461250
three hundred
462250
three hundred
463250
three hundred
464250
three hundred
465250
three hundred
466250
three hundred
467250
three hundred
468250
three hundred
469250
three hundred
470250
three hundred
471250
three hundred
472250
three hundred
473250
three hundred
474250
three hundred
475250
three hundred
476250
three hundred
477250
three hundred
478250
three hundred
479250
three hundred
480250
three hundred
481250
three hundred
482250
three hundred
483250
three hundred
484250
three hundred
485250
three hundred
486250
three hundred
487250
three hundred
488250
three hundred
489250
three hundred
490250
three hundred
491250
three hundred
492250
three hundred
493250
three hundred
494250
three hundred
495250
three hundred
496250
three hundred
497250
three hundred
498250
three hundred
499250
three hundred
for i in range(100,500):
    if i>250:
        print(str(i)+"--250")
    if(i==300):
        print("two hundred")
    if (i>=350):
        print("three hundred")

        
251--250
252--250
253--250
254--250
255--250
256--250
257--250
258--250
259--250
260--250
261--250
262--250
263--250
264--250
265--250
266--250
267--250
268--250
269--250
270--250
271--250
272--250
273--250
274--250
275--250
276--250
277--250
278--250
279--250
280--250
281--250
282--250
283--250
284--250
285--250
286--250
287--250
288--250
289--250
290--250
291--250
292--250
293--250
294--250
295--250
296--250
297--250
298--250
299--250
300--250
two hundred
301--250
302--250
303--250
304--250
305--250
306--250
307--250
308--250
309--250
310--250
311--250
312--250
313--250
314--250
315--250
316--250
317--250
318--250
319--250
320--250
321--250
322--250
323--250
324--250
325--250
326--250
327--250
328--250
329--250
330--250
331--250
332--250
333--250
334--250
335--250
336--250
337--250
338--250
339--250
340--250
341--250
342--250
343--250
344--250
345--250
346--250
347--250
348--250
349--250
350--250
three hundred
351--250
three hundred
352--250
three hundred
353--250
three hundred
354--250
three hundred
355--250
three hundred
356--250
three hundred
357--250
three hundred
358--250
three hundred
359--250
three hundred
360--250
three hundred
361--250
three hundred
362--250
three hundred
363--250
three hundred
364--250
three hundred
365--250
three hundred
366--250
three hundred
367--250
three hundred
368--250
three hundred
369--250
three hundred
370--250
three hundred
371--250
three hundred
372--250
three hundred
373--250
three hundred
374--250
three hundred
375--250
three hundred
376--250
three hundred
377--250
three hundred
378--250
three hundred
379--250
three hundred
380--250
three hundred
381--250
three hundred
382--250
three hundred
383--250
three hundred
384--250
three hundred
385--250
three hundred
386--250
three hundred
387--250
three hundred
388--250
three hundred
389--250
three hundred
390--250
three hundred
391--250
three hundred
392--250
three hundred
393--250
three hundred
394--250
three hundred
395--250
three hundred
396--250
three hundred
397--250
three hundred
398--250
three hundred
399--250
three hundred
400--250
three hundred
401--250
three hundred
402--250
three hundred
403--250
three hundred
404--250
three hundred
405--250
three hundred
406--250
three hundred
407--250
three hundred
408--250
three hundred
409--250
three hundred
410--250
three hundred
411--250
three hundred
412--250
three hundred
413--250
three hundred
414--250
three hundred
415--250
three hundred
416--250
three hundred
417--250
three hundred
418--250
three hundred
419--250
three hundred
420--250
three hundred
421--250
three hundred
422--250
three hundred
423--250
three hundred
424--250
three hundred
425--250
three hundred
426--250
three hundred
427--250
three hundred
428--250
three hundred
429--250
three hundred
430--250
three hundred
431--250
three hundred
432--250
three hundred
433--250
three hundred
434--250
three hundred
435--250
three hundred
436--250
three hundred
437--250
three hundred
438--250
three hundred
439--250
three hundred
440--250
three hundred
441--250
three hundred
442--250
three hundred
443--250
three hundred
444--250
three hundred
445--250
three hundred
446--250
three hundred
447--250
three hundred
448--250
three hundred
449--250
three hundred
450--250
three hundred
451--250
three hundred
452--250
three hundred
453--250
three hundred
454--250
three hundred
455--250
three hundred
456--250
three hundred
457--250
three hundred
458--250
three hundred
459--250
three hundred
460--250
three hundred
461--250
three hundred
462--250
three hundred
463--250
three hundred
464--250
three hundred
465--250
three hundred
466--250
three hundred
467--250
three hundred
468--250
three hundred
469--250
three hundred
470--250
three hundred
471--250
three hundred
472--250
three hundred
473--250
three hundred
474--250
three hundred
475--250
three hundred
476--250
three hundred
477--250
three hundred
478--250
three hundred
479--250
three hundred
480--250
three hundred
481--250
three hundred
482--250
three hundred
483--250
three hundred
484--250
three hundred
485--250
three hundred
486--250
three hundred
487--250
three hundred
488--250
three hundred
489--250
three hundred
490--250
three hundred
491--250
three hundred
492--250
three hundred
493--250
three hundred
494--250
three hundred
495--250
three hundred
496--250
three hundred
497--250
three hundred
498--250
three hundred
499--250
three hundred
for i in range(100,500):
    if i>250:
        print(str(i)+"--250")
    if(i==300):
        print("two hundred")
    if (i>=350):
        print("three hundred")
    if i<=500:
        print("five hundred")

        
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
five hundred
251--250
five hundred
252--250
five hundred
253--250
five hundred
254--250
five hundred
255--250
five hundred
256--250
five hundred
257--250
five hundred
258--250
five hundred
259--250
five hundred
260--250
five hundred
261--250
five hundred
262--250
five hundred
263--250
five hundred
264--250
five hundred
265--250
five hundred
266--250
five hundred
267--250
five hundred
268--250
five hundred
269--250
five hundred
270--250
five hundred
271--250
five hundred
272--250
five hundred
273--250
five hundred
274--250
five hundred
275--250
five hundred
276--250
five hundred
277--250
five hundred
278--250
five hundred
279--250
five hundred
280--250
five hundred
281--250
five hundred
282--250
five hundred
283--250
five hundred
284--250
five hundred
285--250
five hundred
286--250
five hundred
287--250
five hundred
288--250
five hundred
289--250
five hundred
290--250
five hundred
291--250
five hundred
292--250
five hundred
293--250
five hundred
294--250
five hundred
295--250
five hundred
296--250
five hundred
297--250
five hundred
298--250
five hundred
299--250
five hundred
300--250
two hundred
five hundred
301--250
five hundred
302--250
five hundred
303--250
five hundred
304--250
five hundred
305--250
five hundred
306--250
five hundred
307--250
five hundred
308--250
five hundred
309--250
five hundred
310--250
five hundred
311--250
five hundred
312--250
five hundred
313--250
five hundred
314--250
five hundred
315--250
five hundred
316--250
five hundred
317--250
five hundred
318--250
five hundred
319--250
five hundred
320--250
five hundred
321--250
five hundred
322--250
five hundred
323--250
five hundred
324--250
five hundred
325--250
five hundred
326--250
five hundred
327--250
five hundred
328--250
five hundred
329--250
five hundred
330--250
five hundred
331--250
five hundred
332--250
five hundred
333--250
five hundred
334--250
five hundred
335--250
five hundred
336--250
five hundred
337--250
five hundred
338--250
five hundred
339--250
five hundred
340--250
five hundred
341--250
five hundred
342--250
five hundred
343--250
five hundred
344--250
five hundred
345--250
five hundred
346--250
five hundred
347--250
five hundred
348--250
five hundred
349--250
five hundred
350--250
three hundred
five hundred
351--250
three hundred
five hundred
352--250
three hundred
five hundred
353--250
three hundred
five hundred
354--250
three hundred
five hundred
355--250
three hundred
five hundred
356--250
three hundred
five hundred
357--250
three hundred
five hundred
358--250
three hundred
five hundred
359--250
three hundred
five hundred
360--250
three hundred
five hundred
361--250
three hundred
five hundred
362--250
three hundred
five hundred
363--250
three hundred
five hundred
364--250
three hundred
five hundred
365--250
three hundred
five hundred
366--250
three hundred
five hundred
367--250
three hundred
five hundred
368--250
three hundred
five hundred
369--250
three hundred
five hundred
370--250
three hundred
five hundred
371--250
three hundred
five hundred
372--250
three hundred
five hundred
373--250
three hundred
five hundred
374--250
three hundred
five hundred
375--250
three hundred
five hundred
376--250
three hundred
five hundred
377--250
three hundred
five hundred
378--250
three hundred
five hundred
379--250
three hundred
five hundred
380--250
three hundred
five hundred
381--250
three hundred
five hundred
382--250
three hundred
five hundred
383--250
three hundred
five hundred
384--250
three hundred
five hundred
385--250
three hundred
five hundred
386--250
three hundred
five hundred
387--250
three hundred
five hundred
388--250
three hundred
five hundred
389--250
three hundred
five hundred
390--250
three hundred
five hundred
391--250
three hundred
five hundred
392--250
three hundred
five hundred
393--250
three hundred
five hundred
394--250
three hundred
five hundred
395--250
three hundred
five hundred
396--250
three hundred
five hundred
397--250
three hundred
five hundred
398--250
three hundred
five hundred
399--250
three hundred
five hundred
400--250
three hundred
five hundred
401--250
three hundred
five hundred
402--250
three hundred
five hundred
403--250
three hundred
five hundred
404--250
three hundred
five hundred
405--250
three hundred
five hundred
406--250
three hundred
five hundred
407--250
three hundred
five hundred
408--250
three hundred
five hundred
409--250
three hundred
five hundred
410--250
three hundred
five hundred
411--250
three hundred
five hundred
412--250
three hundred
five hundred
413--250
three hundred
five hundred
414--250
three hundred
five hundred
415--250
three hundred
five hundred
416--250
three hundred
five hundred
417--250
three hundred
five hundred
418--250
three hundred
five hundred
419--250
three hundred
five hundred
420--250
three hundred
five hundred
421--250
three hundred
five hundred
422--250
three hundred
five hundred
423--250
three hundred
five hundred
424--250
three hundred
five hundred
425--250
three hundred
five hundred
426--250
three hundred
five hundred
427--250
three hundred
five hundred
428--250
three hundred
five hundred
429--250
three hundred
five hundred
430--250
three hundred
five hundred
431--250
three hundred
five hundred
432--250
three hundred
five hundred
433--250
three hundred
five hundred
434--250
three hundred
five hundred
435--250
three hundred
five hundred
436--250
three hundred
five hundred
437--250
three hundred
five hundred
438--250
three hundred
five hundred
439--250
three hundred
five hundred
440--250
three hundred
five hundred
441--250
three hundred
five hundred
442--250
three hundred
five hundred
443--250
three hundred
five hundred
444--250
three hundred
five hundred
445--250
three hundred
five hundred
446--250
three hundred
five hundred
447--250
three hundred
five hundred
448--250
three hundred
five hundred
449--250
three hundred
five hundred
450--250
three hundred
five hundred
451--250
three hundred
five hundred
452--250
three hundred
five hundred
453--250
three hundred
five hundred
454--250
three hundred
five hundred
455--250
three hundred
five hundred
456--250
three hundred
five hundred
457--250
three hundred
five hundred
458--250
three hundred
five hundred
459--250
three hundred
five hundred
460--250
three hundred
five hundred
461--250
three hundred
five hundred
462--250
three hundred
five hundred
463--250
three hundred
five hundred
464--250
three hundred
five hundred
465--250
three hundred
five hundred
466--250
three hundred
five hundred
467--250
three hundred
five hundred
468--250
three hundred
five hundred
469--250
three hundred
five hundred
470--250
three hundred
five hundred
471--250
three hundred
five hundred
472--250
three hundred
five hundred
473--250
three hundred
five hundred
474--250
three hundred
five hundred
475--250
three hundred
five hundred
476--250
three hundred
five hundred
477--250
three hundred
five hundred
478--250
three hundred
five hundred
479--250
three hundred
five hundred
480--250
three hundred
five hundred
481--250
three hundred
five hundred
482--250
three hundred
five hundred
483--250
three hundred
five hundred
484--250
three hundred
five hundred
485--250
three hundred
five hundred
486--250
three hundred
five hundred
487--250
three hundred
five hundred
488--250
three hundred
five hundred
489--250
three hundred
five hundred
490--250
three hundred
five hundred
491--250
three hundred
five hundred
492--250
three hundred
five hundred
493--250
three hundred
five hundred
494--250
three hundred
five hundred
495--250
three hundred
five hundred
496--250
three hundred
five hundred
497--250
three hundred
five hundred
498--250
three hundred
five hundred
499--250
three hundred
five hundred
for i in range(10,100)
SyntaxError: expected ':'
for i in range(10,100):
    if(i%2==0):
        print(i)

        
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
for i in range(10,100):
    if(i%2==0):
        print(i)
    for x in range (i):
        print(x)

        
10
0
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
6
7
8
9
10
12
0
1
2
3
4
5
6
7
8
9
10
11
0
1
2
3
4
5
6
7
8
9
10
11
12
14
0
1
2
3
4
5
6
7
8
9
10
11
12
13
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
16
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
18
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
20
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
22
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
24
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
26
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
28
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
30
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
32
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
34
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
36
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
38
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
40
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
42
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
44
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
46
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
48
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
50
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
52
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
54
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
56
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
58
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
60
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
62
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
64
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
66
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
68
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
70
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
72
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
74
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
76
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
78
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
80
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
82
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
84
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
86
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
88
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
90
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
92
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
94
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
96
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
98
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98

for i in range(10,100):
    if(i%2==0):
        print("**")
    for x in range (i):
        print("\t")

        
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
**
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
for i in range(10,100):
    if(i%2==0):
        print("**")
    #for x in range (i):
        #print("\t")
        #print(x)
    else:
        print("fail",i)

        
**
fail 11
**
fail 13
**
fail 15
**
fail 17
**
fail 19
**
fail 21
**
fail 23
**
fail 25
**
fail 27
**
fail 29
**
fail 31
**
fail 33
**
fail 35
**
fail 37
**
fail 39
**
fail 41
**
fail 43
**
fail 45
**
fail 47
**
fail 49
**
fail 51
**
fail 53
**
fail 55
**
fail 57
**
fail 59
**
fail 61
**
fail 63
**
fail 65
**
fail 67
**
fail 69
**
fail 71
**
fail 73
**
fail 75
**
fail 77
**
fail 79
**
fail 81
**
fail 83
**
fail 85
**
fail 87
**
fail 89
**
fail 91
**
fail 93
**
fail 95
**
fail 97
**
fail 99
for i in range(10,100):
    if(i%2==0):
        print("**")
    #for x in range (i):
        #print("\t")
        #print(x)
else:
        print("fail",i)

        
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
fail 99
for i in range(10,100):
    if(i%2==0):
        print("**")
    for x in range (i):
        print("\t")
        print(x)
    else:
        print("fail",i)

        
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
fail 10
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
fail 11
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
fail 12
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
fail 13
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
fail 14
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
fail 15
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
fail 16
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
fail 17
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
fail 18
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
fail 19
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
fail 20
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
fail 21
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
fail 22
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
fail 23
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
fail 24
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
fail 25
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
fail 26
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
fail 27
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
fail 28
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
fail 29
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
fail 30
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
fail 31
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
fail 32
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
fail 33
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
fail 34
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
fail 35
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
fail 36
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
fail 37
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
fail 38
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
fail 39
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
fail 40
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
fail 41
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
fail 42
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
fail 43
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
fail 44
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
fail 45
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
fail 46
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
fail 47
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
fail 48
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
fail 49
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
fail 50
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
fail 51
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
fail 52
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
fail 53
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
fail 54
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
fail 55
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
fail 56
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
fail 57
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
fail 58
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
fail 59
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
fail 60
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
fail 61
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
fail 62
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
fail 63
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
fail 64
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
fail 65
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
fail 66
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
fail 67
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
fail 68
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
fail 69
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
fail 70
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
fail 71
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
fail 72
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
fail 73
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
fail 74
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
fail 75
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
fail 76
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
fail 77
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
fail 78
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
fail 79
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
fail 80
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
fail 81
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
fail 82
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
	
82
fail 83
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
	
82
	
83
fail 84
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
	
82
	
83
	
84
fail 85
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
	
82
	
83
	
84
	
85
fail 86
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
	
82
	
83
	
84
	
85
	
86
fail 87
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
	
82
	
83
	
84
	
85
	
86
	
87
fail 88
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
	
82
	
83
	
84
	
85
	
86
	
87
	
88
fail 89
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
	
82
	
83
	
84
	
85
	
86
	
87
	
88
	
89
fail 90
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
	
82
	
83
	
84
	
85
	
86
	
87
	
88
	
89
	
90
fail 91
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
	
82
	
83
	
84
	
85
	
86
	
87
	
88
	
89
	
90
	
91
fail 92
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
	
82
	
83
	
84
	
85
	
86
	
87
	
88
	
89
	
90
	
91
	
92
fail 93
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
	
82
	
83
	
84
	
85
	
86
	
87
	
88
	
89
	
90
	
91
	
92
	
93
fail 94
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
	
82
	
83
	
84
	
85
	
86
	
87
	
88
	
89
	
90
	
91
	
92
	
93
	
94
fail 95
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
	
82
	
83
	
84
	
85
	
86
	
87
	
88
	
89
	
90
	
91
	
92
	
93
	
94
	
95
fail 96
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
	
82
	
83
	
84
	
85
	
86
	
87
	
88
	
89
	
90
	
91
	
92
	
93
	
94
	
95
	
96
fail 97
**
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
	
82
	
83
	
84
	
85
	
86
	
87
	
88
	
89
	
90
	
91
	
92
	
93
	
94
	
95
	
96
	
97
fail 98
	
0
	
1
	
2
	
3
	
4
	
5
	
6
	
7
	
8
	
9
	
10
	
11
	
12
	
13
	
14
	
15
	
16
	
17
	
18
	
19
	
20
	
21
	
22
	
23
	
24
	
25
	
26
	
27
	
28
	
29
	
30
	
31
	
32
	
33
	
34
	
35
	
36
	
37
	
38
	
39
	
40
	
41
	
42
	
43
	
44
	
45
	
46
	
47
	
48
	
49
	
50
	
51
	
52
	
53
	
54
	
55
	
56
	
57
	
58
	
59
	
60
	
61
	
62
	
63
	
64
	
65
	
66
	
67
	
68
	
69
	
70
	
71
	
72
	
73
	
74
	
75
	
76
	
77
	
78
	
79
	
80
	
81
	
82
	
83
	
84
	
85
	
86
	
87
	
88
	
89
	
90
	
91
	
92
	
93
	
94
	
95
	
96
	
97
	
98
fail 99
for i in range(10,100):
    if(i%2==0):
        print("**")
    """for x in range (i):
        #print("\t")
        #print(x)"""
    else:
        print("fail",i)
        
SyntaxError: invalid syntax
for i in range(10,100):
    if(i%2==0):
        print("**")
        """for x in range (i):
        #print("\t")
        #print(x)"""
    else:
        print("fail",i)

        
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 11
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 13
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 15
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 17
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 19
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 21
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 23
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 25
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 27
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 29
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 31
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 33
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 35
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 37
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 39
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 41
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 43
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 45
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 47
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 49
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 51
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 53
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 55
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 57
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 59
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 61
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 63
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 65
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 67
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 69
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 71
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 73
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 75
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 77
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 79
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 81
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 83
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 85
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 87
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 89
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 91
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 93
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 95
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 97
**
'for x in range (i):\n        #print("\t")\n        #print(x)'
fail 99
for num in range(1,101):
    if (num%2=0):
        
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
for num in range(1,101):
    if (num%2==0):
        print("even")
    else:
        print("odd")

        
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
odd
even
for num in range(1,101):
    if (num%2==0):
        print(num,"even")
    else:
        print(num,"odd")

        
1 odd
2 even
3 odd
4 even
5 odd
6 even
7 odd
8 even
9 odd
10 even
11 odd
12 even
13 odd
14 even
15 odd
16 even
17 odd
18 even
19 odd
20 even
21 odd
22 even
23 odd
24 even
25 odd
26 even
27 odd
28 even
29 odd
30 even
31 odd
32 even
33 odd
34 even
35 odd
36 even
37 odd
38 even
39 odd
40 even
41 odd
42 even
43 odd
44 even
45 odd
46 even
47 odd
48 even
49 odd
50 even
51 odd
52 even
53 odd
54 even
55 odd
56 even
57 odd
58 even
59 odd
60 even
61 odd
62 even
63 odd
64 even
65 odd
66 even
67 odd
68 even
69 odd
70 even
71 odd
72 even
73 odd
74 even
75 odd
76 even
77 odd
78 even
79 odd
80 even
81 odd
82 even
83 odd
84 even
85 odd
86 even
87 odd
88 even
89 odd
90 even
91 odd
92 even
93 odd
94 even
95 odd
96 even
97 odd
98 even
99 odd
100 even
for num in range(1,101):
    if (num%2==0):
        print(num,"even")

        
2 even
4 even
6 even
8 even
10 even
12 even
14 even
16 even
18 even
20 even
22 even
24 even
26 even
28 even
30 even
32 even
34 even
36 even
38 even
40 even
42 even
44 even
46 even
48 even
50 even
52 even
54 even
56 even
58 even
60 even
62 even
64 even
66 even
68 even
70 even
72 even
74 even
76 even
78 even
80 even
82 even
84 even
86 even
88 even
90 even
92 even
94 even
96 even
98 even
100 even
for num in range(1,101):
    if (num%2!=0):
        print("odd")

        
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
odd
for num in range(1,101):
    if (num%2!=0):
        print(num,"odd")

        
1 odd
3 odd
5 odd
7 odd
9 odd
11 odd
13 odd
15 odd
17 odd
19 odd
21 odd
23 odd
25 odd
27 odd
29 odd
31 odd
33 odd
35 odd
37 odd
39 odd
41 odd
43 odd
45 odd
47 odd
49 odd
51 odd
53 odd
55 odd
57 odd
59 odd
61 odd
63 odd
65 odd
67 odd
69 odd
71 odd
73 odd
75 odd
77 odd
79 odd
81 odd
83 odd
85 odd
87 odd
89 odd
91 odd
93 odd
95 odd
97 odd
99 odd
for num in range(1,101):
    if (num%2!=0):
        print(num_________,"odd")

        
Traceback (most recent call last):
  File "<pyshell#210>", line 3, in <module>
    print(num_________,"odd")
NameError: name 'num_________' is not defined
for num in range(1,101):
    if (num%2!=0):
        print(num----,"odd")
        
SyntaxError: invalid syntax

for num in range(1,101):
    if (num%2!=0):
        print(num_____,"odd")

        
Traceback (most recent call last):
  File "<pyshell#214>", line 3, in <module>
    print(num_____,"odd")
NameError: name 'num_____' is not defined
for num    in range(1,101):
    if (num%2!=0):
        print(num   ,"odd")for num in range(1,101):
            if (num%2!=0):
                print(num   ,"odd")
                
SyntaxError: invalid syntax

for num... in range(1,101):
    if (num%2==0):
        print(num...,"even")
    else:
        print(num...,"odd")
        
SyntaxError: invalid syntax

for num in range(1,101):
    if (num%2!=0):
        print("....odd")

        
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
....odd
for num in range(1,101):
    if (num%2!=0):
        print(num,"....odd")

        
1 ....odd
3 ....odd
5 ....odd
7 ....odd
9 ....odd
11 ....odd
13 ....odd
15 ....odd
17 ....odd
19 ....odd
21 ....odd
23 ....odd
25 ....odd
27 ....odd
29 ....odd
31 ....odd
33 ....odd
35 ....odd
37 ....odd
39 ....odd
41 ....odd
43 ....odd
45 ....odd
47 ....odd
49 ....odd
51 ....odd
53 ....odd
55 ....odd
57 ....odd
59 ....odd
61 ....odd
63 ....odd
65 ....odd
67 ....odd
69 ....odd
71 ....odd
73 ....odd
75 ....odd
77 ....odd
79 ....odd
81 ....odd
83 ....odd
85 ....odd
87 ....odd
89 ....odd
91 ....odd
93 ....odd
95 ....odd
97 ....odd
99 ....odd
range(10)
range(0, 10)
[rangr(10)]
Traceback (most recent call last):
  File "<pyshell#225>", line 1, in <module>
    [rangr(10)]
NameError: name 'rangr' is not defined. Did you mean: 'range'?
[range(10)]
[range(0, 10)]
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[even(100)]
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    [even(100)]
NameError: name 'even' is not defined

list(range(0,101,2))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
list(range(o,1000,10))
Traceback (most recent call last):
  File "<pyshell#234>", line 1, in <module>
    list(range(o,1000,10))
NameError: name 'o' is not defined
list(range(0,1000,10))
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]
list(range(10,1000,10))
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]
list(range(10,1005,10))
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000]
>>> 
>>> nums=[1,2,5,85,36,7,8,6,7]
>>> for a in nums:
...     print(a)
... 
...     
1
2
5
85
36
7
8
6
7
>>> dir(nums)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(nums.pop)
Help on built-in function pop:

pop(index=-1, /) method of builtins.list instance
    Remove and return item at index (default last).
    
    Raises IndexError if list is empty or index is out of range.

>>> nums=[1,2,5,85,36,7,8,6,7,sd,rom,oiu]
Traceback (most recent call last):
  File "<pyshell#245>", line 1, in <module>
    nums=[1,2,5,85,36,7,8,6,7,sd,rom,oiu]
NameError: name 'sd' is not defined. Did you mean: 'id'?
>>> nums=[1,2,5,85,36,7,8,6,7]
>>> nums.count(" ")
0
>>> len(nums)
9
>>> nums[o]
Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    nums[o]
NameError: name 'o' is not defined
nums[0]
1
nums[3]
85
help(nums.extend)
Help on built-in function extend:

extend(iterable, /) method of builtins.list instance
    Extend list by appending elements from the iterable.

nums=[1,2,5,85,36,7,8,6,7,sd,rom,oiu]
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    nums=[1,2,5,85,36,7,8,6,7,sd,rom,oiu]
NameError: name 'sd' is not defined. Did you mean: 'id'?
nums=[1,2,5,85,36,7,8,6,7,rom,oiu]
Traceback (most recent call last):
  File "<pyshell#254>", line 1, in <module>
    nums=[1,2,5,85,36,7,8,6,7,rom,oiu]
NameError: name 'rom' is not defined
