
#----------------------------LECTURE 1(PRINTING)--------------------------

'''
print('What is your name')
name = input()
print('Hi' ,name +', how are you')
'''



#Input always returns a string.

'''
x='Hello'
print(type(x))

x=7
print(type(x))
'''


#NOTE: Python doesn't have char




#----------------------------LECTURE 2(SEP,DATATYPE)-----------------------

#POINTS:
    #sep(,) has a default value of space(adds a space)
    #There is no signed data types, EVERYTHING is signed


#?????????????????????????????????????????????????????????????????????

#Example: Take two numbers and add them


'''
print('A')
a=int(input('Enter Number One: '))
b=int(input('Enter Number Two: '))
print('\nAddition of',a,'and',b,'is',a+b)
'''

#?????????????????????????????????????????????????????????????????????


#NOTE: input() function leaves a line before executing


'''
print("Hello","World",sep=("****"))
'''


#sep(,) has a default value of " " but you can change


'''
print("Hello","World",sep=("****"),end=(" END "))
print("Second line")
'''

#***************************DEFINITIONS*******************************

##Data Types =>
'''
int()
float point numbers
complex numbers
string is basic data type
boolean
'''
##Operators =>


#Division: will always result in float and NEVER in int like observed in C programming
'''E,g.:
    
print(22/7)
print(4.6%1.5)
print(22.0%7)
'''
#NOTE: If both operands are integers output is also integer but even if one is float output will be float


#Floor Division(//): Floor is the largest integer lower than and decimal number
                    #Eg. 2.3 has a FLOOR of '2' and CEILLING of '3'

'''#Eg:

print(22//7)
print(-22//7)
print(22//-7)

a/b remainder = r and quotient = d(Floor division)
a=b*d+r
r=a-b*d
'''

#Floor Division Q:
    
'''
print(23%5)
# 23%5 => 23-(5)*(4) = 3
print(-23%5)
# -23%5 => -23-(5)*(-5) = 2
print(23%-5)
# 23%-5 => 23-(-5)*(-5) = -2
print(-23%-5)
# -23%-5 => -23-(-5)*(4) = -3
'''


#*********************************************************************




#----------------------------LECTURE 3(OPERATORS)--------------------------------


#****************************DEFINITIONS************************************


#Expoonent operator (**) --> 5**2 will give 25
'''#E.g.
print("Square of 5 is",5**2)
'''

#Relational Operator: 
    #In python, "and", "not", and "or" have to be written instead of "&&","!", and "||"

    #Bitwise operators are the identically same


#is operator: Same address results in True
    
#is not operator:
    
#in: Checks if the letter or string is in the main string
    
#not in: Inverse of "in"

#id fuinction: Tells the address of the variable

#*************************************************************************


'''#E.g.
a=10
b=10
a+=5
print(a is b)  --> Gives True

a=10
b=10
a+=5
print(a is b)  --> Give False

NOTE: When saying a=10, 10 is created and "a" points to it but, if we say b=10 
      "b" will also point at the same place(It doesnt make a copy of 10). But
      when we say a+=5, a new 15 is created and a points to it now.
'''


#Memory allocation example:
'''
a=10
while a>0:
    print(a)
    print(id(a))
    a-=1
'''




#----------------------------LECTURE 4(CONDITION STATEMENTS)----------------------------------


#****************************DEFINITIONS************************************

#Statements:
#   "Statements" are executed if "test expression" is true

# Pass: Doesnt do anything
#    In some situations statements doesnt allow no statements, if you intend to do nothing we can use pass

#***************************************************************************


'''
Question 1: 


marks = int(input("ENter your marks:  "))

if marks >= 60:
    print("You have passed with first class")
    
if marks >= 50 and marks < 60:
    print("You have passed with second class")
    
if marks >= 40 and marks<50:
    print("You have passed with third class")
    
if marks < 40:
    print("You have Failed :(")

'''


# elif: is used for nested if else loops


'''
Question 2:

marks = int(input("Enter your marks:  "))

if marks >= 60:
    print("You have passed with first class")
    
elif >= 50:                                         !!!We dont need to check
    print("You have passed with second class")
    
elif >= 40:
    print("You have passed with third class")
    
else:
    print("You have Failed :(")
    print("Better luck next time!!!")

'''


'''
#E.g. (While Loop)

a=int(input("Enter a number: "))
i=1
while i<=10:
    print(a,"x",i,"=",a*i)
    i+=1

'''

'''
#E.g. (Continue Statement)

a=int(input("Enter a number: "))
i=0
while i<10:
    i+=1
    if i==4:
        continue
    print(a,"x",i,"=",a*i)

'''

'''
#E.g. (Break Statement)

a=int(input("Enter a number: "))
i=0
while i<10:
    i+=1
    if i==4:
        break
    print(a,"x",i,"=",a*i)

else:
    print("into else part of while loop")
print("Outside while loop")

'''


'''
Questoin 3:
'''
'''
import random

x = random.randint(0,1000)
guess = int(input("Enter your guess: "))

print(x)

while guess != x:
    
    if guess > x:
        print("Guess a smaller number.")
        
    elif guess < x:
        print("Guess a bigger number.")
        
    guess = int(input("Enter number:  "))

else:
    print("Congratulations! You have found the number.")
'''


'''
import random 

x= random.randint(0,1000)
guess=int(input("Enter your guess: "))
while guess!=x:
    if guess > x:
        print("Think of a smaller number")
    elif guess <x:
        print("Think of a bigger number")

    guess=int(input("Enter your guess: "))

else:
    print("You guessed it correct")
'''




#----------------------------LECTURE 5(FOR LOOP)---------------------------------


#For Loop:
#   Completely Different than in c
#   Usually used for scanning


'''
E.g.
    
for c in "Hello, World!"
    print(c)
'''


#list syntax and using For loop with list


'''
list = [1,8,6,7,4,2,3]

for i in list:
    print(i)
'''


#Range Function:
#   Generates a sequence of numbers.


'''
for i in range(10):
    print(i)

print("\n")

for i in range(10,20):
    print(i)

print("\n")

for i in range(0,100,5):
    print(i)
'''

##NOTE: The third parameter can be negative

'''
for i in range(100,50,-5):
    print(i)
'''

##NOTE: "Range" does not take float values

'''
for i in range(0.5,10)
    print(i)
'''


#????????????????????????????????????????????????????????????????????????????

#Armstrong Numbers


'''
for i in range(1,10000):
    temp = i
    sum = 0
    l = len(str(i)) 

    while temp > 0:
        num = temp%10
        sum += num**l
        temp //= 10
    if sum == i:
        print(i,"is an Armstrong Number")   
'''
'''
for i in range(1,10000):
    s = str(i)
    sum = 0
    l = len(s) 

    for c in s:
        sum += c**l

    if sum == i:
        print(i,"is an Armstrong Number")   
'''


#????????????????????????????????????????????????????????????????????????????




#----------------------------LECTURE 5(STRINGS)---------------------------------


#Indexing of a String:
#   print(string[position]) will print the letter at that position in the string.

'''
Eg:
'''
'''
string = "Hello world, how are you?"

print(string[0])                    # Will print "H"
print(string[10])                   # Will print "d"
print(string[18])                   # Will print "r"
'''


#Slicing:
#   print(string[pos1:pos2]) will print all the letters from positon pos1 to pos2.

'''
string = "Hello world, how are you?"

print(string[2:5])                  # Will print "llo w"
print(string[8:10])                 # Will print "rl"
print(string[7:18])                 # Will print "orld, how are you"
print(string[2:])                   # Will print "llo world, how are you?" 
print(string[:10])                  # Will print "Hello world?" 
print(string[1:20])                 # WILL GIVE AN ERROR!!! 
'''

##NOTE: Python has bound checking
##NOTE: Blank parameter would let it take "0" and "Last position" as parameters for start and end respectively

'''
s = "Hello world, how are you?"

print(s[:18:5])                # Will print "H dw "
print(s[5:15:2])               # Will print " ol,hw" | Will print " ol,hwae"
print(s[20:10])                # WONT PRINT ANYTHING
print(s[20:10:-1])             # Will print " era woh ,"
print(s[18:10:-1]+"*")         # Will print " r o"
print(s[::-1])                 # Will print "?uoy era woh ,dlrow olleH"
'''



#----------------------------LECTURE 6 & 7(FUNCTIONS)---------------------------------


# .CSV: 
#   Coma Seperated File

#Split:
#   Would split a string at the given parameter("word")


'''
#Spliting String:

string = "Hello how are you?"
a = string.split(" ")
print(a)
'''

'''
#Joining Of Strings:

string = "Hello how are you?"
a = string.split(" ")           #Spliting the String
new = a.join("...")             #Joining with list elements with "..."
print(new)

#Optimising the above code:

s="Hello How are you"
print(' '.join(s.split()[::-1]))
'''


'''
Capitalize()    (Capitalise First Letter)
Upper()         (Capitalize Everything)
Lower()         (Lower size everything)
Title()         (First Letter Of All Words Increase)
Swapcase()      (Lower to upper and Upper to Lower)

center(int_spaces)        (Gives spaces before and after the string)
ljust()                   (Gives spaces to the left of the string)
rjust()                   (Gives spaces to the right of the string)

strip("anything")            (Removes the characters in the string inf the parameters before and after the string)
strip()                      (Removes the white spaces before and after the string)
lstrip()                     (Removes the white spaces to the left of the string)
rstrip()                     (Removes the white spaces to the right of the string)
'''

'''
E.g. [Center()]
'''
'''
string = "Hello how are you?"
print(string.center(50), "over")
print(string.ljust(50), "over")
print(string.rjust(50), "over")
'''

'''
E.g. (Strip())
'''
'''
string = "                Hello how are you                 "
print(string.strip(),"over")
print(string.lstrip(),"over")
print(string.rstrip(),"over")
'''




#----------------------------LECTURE 8(F.STRING_FORMAT)---------------------------------


'''
#format()
# we have to give a template string
#template.format()

a = 20
b = 73.9758
c = "Hello World"
print(a,b,c)

# this is called as a template string ; {} are called as placeholders
s = "a = {} b = {} c = {}".format(a,b,c)
print(s)

s = "a = {0} b = {1} c = {2}".format(a,b,c)
print(s)


s = "a = {0} b = {0} c = {0}".format(a,b,c)
print(s)

s = "a = {2} b = {1} c = {0}".format(a,b,c)
print(s)


s = "a = {0:5d} b = {1} c = {2}".format(a,b,c)
print(s)

s = "a = {0:15d} b = {1} c = {2}".format(a,b,c)
print(s)


b = 73.9758
s = "a = {0:5d} b = {1:10.3f} c = {2}".format(a,b,c)
print(s)


s = "a = {0:5d} b = {1:10.5f} c = {2}".format(a,b,c)
print(s)


s = "a = {0:5o} b = {1:10.5f} c = {2}".format(a,b,c)
print(s)


s = "a = {0:5x} b = {1:10.5f} c = {2}".format(a,b,c)
print(s)

s = "a = {0:5b} b = {1:10.5f} c = {2}".format(a,b,c)
print(s)

# d = decimal; o = octal; b = binary; x = hexadecimal; f = float


#justification: '<'= left justify ; '>' = right justify ; '^' = center justify
s = "a = {0:<25d} b = {1:10.3f} c = {2}".format(a,b,c)
print(s)

s = "a = {0:>25d} b = {1:20.3f} c = {2}".format(a,b,c)
print(s)

s = "a = {0:^25d} b = {1:^10.3f} c = {2}".format(a,b,c)
print(s)
'''

'''
s = input("String: ")
t = len(s)
if t >=3:
    if s.endswith("ing"):
        print(s+"ly")
    else:
        print(s+"ing")
else:
    print(s)
'''

'''
s = input("String: ")
print(s.find("not"),s.find("poor"))
t = s.find("not")
p = s.find("poor")

if t != -1 and t < p and p >=0:  
    s = s.replace(s[t:p+4],"good")
print(s)
'''




#----------------------------LECTURE 9(MATH_MODULE)---------------------------------


'''
math.e      => 
math.pi     =>
math.tau    =>
math.inf    =>
math.nan    => 
'''


'''
math.degrees()  => Convert to degrees
math.radians()  => Convert to radians
'''


'''
math.sin()  => Returns sine of an angle in radians
math.cos()  => Returns cosine of an angle in radians
math.tan()  => Returns tangent of a number
'''

'''
import math

print(math.sin(math.radians(30)))
print(math.cos(math.radians(30)))
print(math.tan(math.radians(30)))
'''


'''
import math

d = 30
r = math.radians(d)
t = math.tan(r)
r1 = math.atan(t)
d1 = math.degrees(r1)
print(d1)
'''




#----------------------------LECTURE 8(RANDOM)---------------------------------


'''
import random
l = [1,2,3,3.5,"Hello",7,5.6,7.3]
for i in range(10):
    print(random.choice(l))

print(l)
random.shuffle(l)
print(l)
'''




#----------------------------LECTURE 8(TUPLES_AND_LISTS)---------------------------------


#****************************DEFINITIONS************************************

#Tuple:
#   Each element has a UNIQUE ID
#   Written with ROUND BRACKETS
#   They are IMMUTABLE
#   Accessing the element will be done by tuple_name['index']  (SAME AS LISTS)
#   Tuple can contain another tuple

#Tuple Slicing: (SAME AS STRINGS)



#***************************************************************************




#----------------------------LECTURE 9(LISTS)---------------------------------


#****************************DEFINITIONS************************************

# LISTS:
# Ways of initialisation:
    # l1 = []
    # l2 = list()
    # l3 = [10, 20, 30]
    # l4 = list(range(10))      => List of 10 elements
    # l5 = list("abcdefgh")     => Stores string in list
    # l6 = eval(input())        => Input is stored in list
    # l7 = [26, 34]*5           => Multiplies whole list with 5

        # [26, 34]*5   =>  [26,34,26,34,26,34,26,34,26,34,]

# Addition is allowed:

    # A = [1,2,3]
    # B = [4,5]
    # C = [1,2,3,4,5]

# List have INDEX
# Lists are MUTABLE


# l1.Append()  => Adds at the end of the string

'''
l1 = [1,2,3]
l1.append(4)
print(l1)

# Input => [1,2,3,4]
'''

# l1.Insert()  => Adds at the beginning of the string

'''
l1 = [1,2,3]
l1.insert(1,10)
print(l1)

# Input => [1,10,1,2,3,4]
'''

# l1.Extend  => Adds elements of iterable at the end of the list

'''
l1 = [1,2,3]
l1.extend([10,20,30])
l1.extend("Hello World")
print(l1)
'''

# l1.remove('element')  => Removes the first occurence of 'element'

# pop()
# By default it returns and removes the last element of the list
# If index given the element at that position is removed


# delete(l1[index])  => deletes element at the index in list l1
#   If given only the list without any index the whole list is deleted

'''
l1 = [1,2,3,4,5,6]
del(l1[-1])             => deletes element at -1
del(l1[2])              => deletes element at 2 
del(l1)                 => deletes the whole list
del(l1[2:4])                 => deletes the elements in the range
print(l1)
'''

'''
3 = [1,5.6,10]
print(len(l3))
print(max(l3))
print(min(l3))
print(sum(l3))

l4 = ["him","why","his","?",","]
print(len(l4))
print(max(l4))
print(min(l4))
# print(sum(l4))

# in strings, max and min are acc. to alphabetical order
'''

#***************************************************************************




#----------------------------LECTURE 9(LISTS)---------------------------------


'''
import random
l = list(range(100))
for i in range(100):
    l[i] = random.randint(0,50)
print(str(l)+"\n"+str(l.count(10)))
'''


'''
import random
l = list(range(100))
a = 0

for i in range(100):
    a = random.randint(0,50)
    l[i] = a
tup = set(l)
s1, s2, s3, s4, s5 = 0, 0, 0, 0, 0

for j in tup:
    if j<=10:
        s1 += l.count(j)
    elif j<=20:
        s2 += l.count(j)
    elif j<=30:
        s3 += l.count(j)
    elif j<=40:
        s4 += l.count(j)
    else:
        s5 += l.count(j)
print(l)
print("01 to 10 :", s1)
print("11 to 20 :", s2)
print("21 to 30 :", s3)
print("31 to 40 :", s4)
print("41 to 50 :", s5)
print(tup)
'''


'''
import random
l1 =[]
l2 = []
for i in range(100):
    l1.append(random.randint(0,9))
for i in range(10):
    l2.append(l1.count(i))
print(l1)
print(l2)
'''


'''
import random
l1 =[]
l2 = list(range(10))
for i in range(100):
    l1.append(random.randint(0,9))
    l2[l1[i]] += 1
print(l1)
print(l2)
'''

'''
a = int(input())
num = []
while a!=0:
    num.append(a)
    a = int(input())
num.sort()
print(num[-2])
'''




#----------------------------LECTURE 9(LISTS)---------------------------------



#****************************DEFINITIONS************************************


'''
def MyFunction(s):
    return s[-1]

l = ["Hello","Is","you","Your","Python","are"]
#       e      s    o      o      y       r
l.sort(key=MyFunction)
print(l)
'''


'''
def Sorting(l):
    
    return sum(l)

#l=[[10,20,30],[50,60],[5.6,-2,-10],[40,100,200],[10,20,50]]
#l.sort(key= lambda l:l[1])
#print(l)

l=[[10,20,30],[50,60],[5.6,-2,-10],[40,100,200],[10,20,50]]
#l.sort(key=Sorting)
#print(l)

#l.sort(key=lambda l:sum(l))
#print(l)

l.sort(key=sum)
print(l)
'''


'''
def SumDigit(n):
    s=0
    for x in str(n):
        s+=int(x)
    return s

l = [1234,999,783,54947,112345568]
#     10  27   18   29     35
l.sort(key=SumDigit)
print(l)
'''


'''
def SumDigit(n):
    s=0
    for x in str(n):
        s+=int(x)
    return sum([int(x) for x in str(n)])

l = [1234,999,783,54947,112345568, 11234, 2345,99]

#     10  27   18   29     35        11    14  18
l.sort(key=SumDigit)
print(l)
'''


'''
def SumDigits(n):
    s = 0
    for x in str(n):
       s += int(x)
    return s


l = [1234, 999, 783]
l.sort(key=SumDigits)
print(l)
'''


'''
def SumDigits(n):
    return sum(int(x) for x in str(n))          # List Comprehension


l = [1234, 11234, 783]
l.sort(key=SumDigits)
print(l)
'''


#***************************************************************************




#----------------------------LECTURE 10(SCRAPING)---------------------------------

'''
from typing import Collection
'''

mydata = '''12010244,B,1,AROLE ROHIT VASANT
12010218,B,2,ARUNAV CHANDRA
12011397,B,3,ARYAN ATUL MAHAJAN
12010942,B,4,ARYAN VISHVAS KOSHATWAR
12011303,B,5,ASHFAN KHAN ASHFAQUE KHAN
12010550,B,6,ASORE AVDHUT DNYANOBA
12010727,B,7,ATHALYE GARGEE VASUDEO
12010114,B,8,ATHARVA ANIL VIBHUTE
12010264,B,9,ATHARVA MUGALIKAR
12011209,B,10,ATHARVA POPATRAO SARDE
12010236,B,11,ATHARVA PRADEEP GADEKAR
12010954,B,12,ATRAM PRAJWAL PUNDLIK
12011176,B,13,AURANGABADKAR GAYATRI SATISH
12010694,B,14,AWALE CHINMAYEE MILIND
12010676,B,15,AWALE SAKSHI VISHWAS
12010955,B,16,AWALEKAR HARSHADA SURESH
12011372,B,17,AYUSH SINGH NEGI
12010001,B,18,AYUSH VISPUTE
12010655,B,19,AYUSHI KHARE
12010673,B,20,BABAR SOHAM DATTATRAY
12011265,B,21,BABLADKAR SAHIL KISHORE
12010348,B,22,BACHHAV DARSHAN PRAVIN
12011046,B,23,BADE SAKSHI AMBADAS
12011094,B,24,BADGUJAR MAYUR SUDHIR
12010486,B,25,BADHE TEJAS RAVINDRA
12011098,B,26,BADRE BHAVESH NITIN
12010730,B,27,BAGADE AWANTI ARVIND
12011240,B,28,BAGBAN ABUBAKAR SIDDIQ
12010801,B,29,BAGUL VIVEK VIJAY
12010744,B,30,BAHURE SANSKRUTI VITTHALSING
12011000,B,31,BALI SHRUTI HEMANTKUMAR
12010803,B,32,BALSHETWAR YASH SHANKAR
12010463,B,33,BANDE ATHARVA DADABHAU
12010949,B,34,BANG TILAK GIRISHKUMAR
12011371,B,35,BANGAD KHUSHI SURENDRAKUMAR
12010882,B,36,BANGAR SHUBHAM BHAGWAT
12010412,B,37,BANKAR YASHODHAN NIRANJAN
12010649,B,38,BANNORE PRATHAM AJITKUMAR
12010926,B,39,BANSAL MOHANJEETSINGH BHUPENDRASINGH
12010411,B,40,BARADKAR KARTIK DILIP
12010367,B,41,BARANJALEKAR ISHWARI VILAS
12010952,B,42,BARAVKAR PREM BALASAHEB
12010736,B,43,BARGAJE AKSHAY KESHAV
12010451,B,44,BARI NAYAN SATISH
12010873,B,45,BARMADE SHREYAS RAJENDRA
12010568,B,46,BARU HARSHAL SANJAY
12010651,B,47,BARVE APOORVA PRAVEEN
12010593,B,48,BAVISKAR YASH MANOJ
12011339,B,49,BELORKAR OM PARAG
12010226,B,50,BHADANE PAVANKUMAR ROHIDAS
12010665,B,51,BHADANGE AKASH PRAKASH
12010525,B,52,BHAGWAT AMRUT AJIT
12011062,B,53,BHAGWAT SAKSHI UMESH
12010005,B,54,BHAKE SARTHAK SUJIT
12010562,B,55,BHALERAO APURVA VILAS
12011235,B,56,BHALERAO SIDDHANT VIJAY
12010846,B,57,BHARTIYA ADITYA JAGDISH
12010010,B,58,BHAT TEJAS DINESH
12010747,B,59,BHATTAD RESHAM OMPRAKASH
12010370,B,60,BHATTI SUKHPREET SINGH SANTOSH SINGH
12010150,B,61,BHAVE AMEYA HEMANT
12010510,B,62,BHAVE SOHAM SHRIRANG
12010703,B,63,BHAWALKAR TANMAY TUSHAR
12011070,B,64,BHILWANDE ABHISHEK BHASKAR
12011347,B,65,BHIMANWAR TANMAY ASHISH
12010432,B,66,BHOIR VEDANT LAXMAN'''


'''
l1 = mydata.split('\n')
l2 = []
for i in l1:
    a = i.split(',')
    l2.append(tuple(a))
print(l2)
'''

'''
rnum = input()
for i in l2:
    if i[2]==rnum:
        print(i[3])
'''

'''
name = input()
name = name.upper()
for i in l2:
    if name in i[3]:
        print(i)
'''

'''
name = input()
name = name.upper()
for i in l2:
    if name in i[3]:
        print("{:12s}{:2s}{:>5s}\t{:20s}".format(i[0],i[1],i[2],i[3]))
'''

'''
l2 = l2.sort(key= lambda t:t[0])
print(l2)
'''




#----------------------------LECTURE 10(LISTCOMPRIHENSION)---------------------------------

# 1.
'''
l1 = list(range(10))
print(l1)
'''

# CAN ALSO BE WRITTEN AS

# L = [<expression> for <element> in <sequence> if <condition>]
'''
L = [i for i in range(10)]
print(L)
'''


# 2.
'''
l = []
for i in range(10):
    l.append(i**2)
print(l)
'''

# CAN ALSO BE WRITTEN AS

# L = [<expression> for <element> in <sequence> if <condition>]
'''
l = [i**2 for i in range(10)]
print(l)
'''


# 3.
'''
l = []
for i in range(21,51):
    if i%3==0:
        l.append(i**2)
print(l)
'''

# CAN ALSO BE WRITTEN AS

# L = [<expression> for <element> in <sequence> if <condition>]
'''
l = [i**2 for i in range(21,51) if i%3==0]
print(l)
'''


# 4.
'''
t1=[10,20,33,20.4,44.5]
t2=[i*1.8+32 for i in t1]
print(t2)
'''




#----------------------------LECTURE 11(RANDOM)---------------------------------


'''
t = input().split()
x = []
for i in t:
    x.append(int(i))
print(t)
print(x)
'''


'''
t = input().split()
for i in range(len(t)):
    t[i] = int(t[i])
print(t)
'''


'''
t = [int(i) for i in input(" Enter numbers: ").split()]
print(t)
'''


'''
different ways to print a list:

l = [0]*10
#print(l)


l2 = []
for i in range(10):
    l2.append(0)
#print(l2)


l3 = [0 for i in range(10)]
#print(l3)


import random 
l4 = []
for i in range(10):
    l4.append(random.randrange(1,100))
#print(l4)


l5 = [random.randrange(1,100) for i in range(10)]
#print(l5)
'''


'''
# pass or fail
marks = [20, 50, 70, 85, 60,33, 28 , 55, 48,36, 73]

def result1(marks1):
    if marks1 >=40:
        return "Pass"
    else:
        return "Fail"
    
result2 = list(map(result1,marks))
#print(result2)


result = []
for i in marks:
    if i <=40:
        result.append("Fail")
    else:
        result.append("Pass")
#print(result)


result3 = list(map(lambda m:"Pass" if m>40 else "Fail", marks))
#print(result3)

result4 = ["Pass" if m>40 else "Fail" for m in marks]
print(result4)
'''


'''
#problem: filter the marks which have passed among all marks

result5 = list(filter(lambda m: m >=40, marks))
#print(result5)

result6 = [m for m in marks if m >=40]
print(result6)
'''

'''
l1 = [[10,20,30],[40,50],[60,70,80,90]]
l2 = [j for i in l1 for j in i if len(i)>=3]
print(l2)
'''


'''
# Generate a list  [0,  0, 1,   0, 1, 2,    0, 1, 2, 3,    0, 1, 2, 3, 4]
# Note :  Additional spaces are added to clearly explain the pattern, 
# the actual list will not have those additional spaces

n = int(input("Enter number: "))
l = []
for i in range(n+1):
    for j in range(i):
        l.append(j)
print(l)


# Alterntive Way
n = int(input())
l = [j for i in range(n+1) for j in range(i)]
print(l)
'''




#----------------------------LECTURE 12(DICTIONARY)---------------------------------


#****************************DEFINITIONS************************************

'''
# Declaring Dictionary
d = {"key":"value"}

# Empty Dictionary
d = {}
d = dict()

# Declaring and initialisation
d = {'X':100,'Y':100}
'''

# Value can be called using the key
# Anything IMMUTABLE can be a key
# A key has to be UNIQUE
# The VALUE can be anything i.e. mutable or immutable

'''
d = {'X':100,'Y':100}
d['Z'] = 100
d['X'] = 200                        # Updates value of 'key X' from 100 to 200
print(d)
'''

'''
# Update:
d1 = {'X':100,'Y':100}
d2 = {'Z':200, 'X':500} 
d1.update(d2)                       # Updates d1 dictionary by d2

# Update would update the value for 'X' ONLY IF the vale is different in d2
# Update would also append the "'Z':200" to d1 since d1 doesnt exist in d1
print(d1)
'''


# Deleting: 2 ways, 'del' and 'pop'
# del:
# Removes the key-value pair
# Gives error if key doestn exist
'''
d = {'X':100,'Y':100}
# del d[<key>]                      # Syntax
del d['X']                          # This line would delete the value AND key 'X'
print(d)
'''

# pop:
# Returns the key-value pair removed
# Error wont be given if the default value is given, but the default value will be returned
'''
d = {'X':100,'Y':100}
# d.pop(<key>[,<Default>])                          # Syntax
returned_val = d.pop('X','error')                          
print(returned_val)                                 # Will print 100 and also remove 'X':100 key-value pair

d = {'X':100,'Y':100}
returned_val = d.pop('Z','not found')
print(returned_val)                                 # Will print 'not found'
'''

'''
# popitem():
# Removes key-value pair randomly
# Returns tuple of key-value pair removed
# 
d = {'X':100,'Y':100}
returned_val = d.popitem()
print(returned_val)                                 # Will remove and print random key-value pair
'''





#***************************************************************************


'''
# Eg
numbers = {"Atharva":8999965642, "Shruti":7952481233, "Sanskruti":9351225135}
days = {"Jan":31, "Feb":28, "Mar":31}
'''




#----------------------------LECTURE 13(DICTIONARY)---------------------------------

'''
points = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2, 'H':4, 
          'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1, 'O':1, 'P':3, 
          'Q':10, 'R':1, 'S':1, 'T':1, 'U':1, 'V':4, 'W':4, 'X':8,
          'Y':4, 'Z':10}

word = input().upper()
score = 0
for i in word:
    score += points[i]
print(score)
'''


'''
# Find length of a sentence

#method 1
sentence_list = input("Give a sentence: ").split()
dictionary = {}
for i in sentence_list:
    dictionary[i]=len(i)
print(dictionary)
#method 2
d = {i : len(i) for i in input("Enter a string: ").split()}
print(d)
'''


'''
# printing a dictionary of letters and their ASCIi values*

print({chr(i): i for i in range(ord('A'),ord('Z')+1)})
'''


'''
points = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2, 'H':4, 
          'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1, 'O':1, 'P':3, 
          'Q':10, 'R':1, 'S':1, 'T':1, 'U':1, 'V':4, 'W':4, 'X':8,
          'Y':4, 'Z':10}

x = points.keys()
#print(x)
#print(type(x))
#print(list(x))

y = points.values()
#print(y)
#print(type(y))
#print(list(y))

z = points.items()
#print(z)
#print(type(z))
#print(list(z))

'''

'''
l = [list(points.keys()) for i in list(points.values()) if i>=5] #wrong
print(l)

l=[i for i in points if points[i]>=5]
print(l)
'''

'''
z = list(points.items())
z.sort(key = lambda i: i[1] ,reverse=True)
print([i[0] for i in z])
'''




#----------------------------LECTURE 14(DICTIONARY)---------------------------------


'''
# Reading the file: "poem.txt"
f = open('poem.txt')
txt = f.read()
print(txt)
f.close()

# Replace Punctuations
from string import punctuation
punctuation += '?????????'
for i in punctuation:
    txt = txt.replace(i,"")
print("\n"+txt)

# Put words in List
l = txt.split()
print(l)
'''


'''
# Create a dictionary with words as keys and their count as value

# Reading the file: "poem.txt"
f = open('poem.txt')
txt = f.read()
f.close()

l = txt.split()
d = {}

for i in l:
    # if i in d:
    #     d[i] += 1
    # else:
    #     d[i] = 1

    ### Can Also Be Written As:
    d[i] = (d[i]+1) if i in d else 1
    

print(d)
'''




#----------------------------LECTURE 15(SET)---------------------------------

# Set is a Collection
# Repeatation or duplication of elements isnt possible
# Set is Unordered
# Sets are MUTABLE
# If you try to repeat elements it wont give error


# Syntax:
# 1. Creating set of homogeneous elements:
'''
s = {1,2,3,4}
print(s)
'''

# 2. Creating empty set:
'''
s = set()
print(s)
'''

# 3. Adding elements:
# Syntax:
'''
x.add('Element')
'''

# 4. Adding Iterrables:
# Syntax:
'''
x.update("ITERRABLE")
'''

'''
# E.g.
x = {'A','B','C'}
x.update([1,2,3])
print(x)
'''


# REMOVE:

# Removes given item from set
# If item doesnt exist, NO ERROR REPRETED


# POP:

# Removes a random element from the set
# Returns the removed element

'''
A = set()
A.pop()                    # Gives an error
'''


#### NOTE!!!!!
    # NEVER USE,   MUTABLE1 = MUTABLE2,  REFERENCE GETS COPIED AND GIVES PROBLEMS




#----------------------------LECTURE 16(FUNCTION)---------------------------------


# Compact code.
# Reusability.
# 


# Syntax:
# def <name_of_funct.>(<Parameters>)


'''
# E.g.
# funct. for adding 3 numbers:
def add_3(x, y, z):
    addition = x+y+z
    return addition


# Taking Input
a = int(input())
b = int(input())
c = int(input())

# calling 'add_3' function
print(add_3(a, b, c))
'''


# x=10 will make sure even if user doesnt give input it has an value of 10 by default
'''
def funct(x=10):
    print(x)
'''

# Condition 1:
# not passing any value
'''
funct()
'''

# Condition 2:
# Since argument is given x wont be 10 by default but will take the value 100
'''
funct(100)
'''


# Write a function to give the factoria
'''
def fact(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod


# Input
num = int(input("Enter a number: "))
print(f'The factorial of {num} is:',fact(num))
'''




#----------------------------LECTURE 17(RECURSION)---------------------------------


# Function calling itself  -_-


