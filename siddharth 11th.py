#1 Read a text file line by line and display each word separated by a #.

"""
def WordsSeparated():
    f=open("abc.txt","r")
    while True:
        line=f.readline()
        if line=='':
            break
        else:
            words=line.split()
            for i in words:
                print(i+'#',end='')
            print()
    f.close()
WordsSeparated()
"""


#2 Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file

"""
def vcul():
    f=open("abc.txt","r")
    V=C=U=L=0
    data=f.read()
    for i in data:
        if i.isalpha():
            if i.isupper():
                U+=1
            if i.islower():
                L+=1
            if i.lower() in 'aeiou':
                V+=1
            else:
                C+=1
    print("Vowels = ",V)
    print("Consonants = ",C)
    print("Uppercase =",U)
    print("Lowercase",L)
vcul()
"""


#3 Remove all the lines that contain the character 'a' in a file and write it to another file

"""
def Remove():
    fo=open("old.txt","r")
    fn=open("new.txt","w")
    L=[]
    lines=fo.readlines()
    for line in lines:
        if 'a' in line:
            fn.write(line)
        else:
            L.append(line)
    fo = open("old.txt", "w")
    fo.writelines(L)
    fo.close()
    fn.close()
Remove()
"""

#4 Create a binary file with name and roll number. Search for a given roll number and display the name, if not found display appropriate message.

"""
import pickle
def write():
    f=open("StudentDetails.dat","wb")
    while True:
        r=int(input("Enter Roll Number : "))
        n=input("Enter Name : ")
        Data=[r,n]
        pickle.dump(Data,f)
        ch=input("More ? (Y/N)")
        if ch in 'Nn':
            break
    f.close()
    
def Search():
    found=0
    rollno=int(input("Enter roll number : "))
    f = open("StudentDetails.dat", "rb")
    try:
        while True:
            rec=pickle.load(f)
            if rec[0]==rollno:
                print(rec[1])
                found=1
                break
    except EOFError:
        f.close()
        if found==0:
            print("Sorry....No record found")
            
            
write()
Search()
"""

#5 Create a binary file with roll number, name and marks. Input a roll number and update the marks

#6 Write a random number generator that generates random numbers between 1 and 6 (simulates a dice)
"""
def random():
    import random
    s=random.randint(1,6)
    return s
print(random()) 

"""


xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

"""


 Write a Program to show whether entered numbers are prime or not in the given range.
 
Download
lower=int(input("Enter lowest number as lower bound to check : "))
upper=int(input("Enter highest number as upper bound to check: "))
c=0
for i in range(lower, upper+1):
     if (i == 1): 
          continue
  
# flag variable to tell if i is prime or not 
     flag = 1
          
     for j in range(2, i // 2 + 1): 
          if (i % j == 0): 
               flag = 0
               break
              
# flag = 1 means i is prime 
# and flag = 0 means i is not prime 
     if (flag == 1): 
          print(i, end = " ") 

2. Input a string and determine whether it is a palindrome or not.
 
Download
string=input('Enter a string:')
length=len(string)
mid=length//2
rev=-1
for a in range(mid):
     if string[a]==string[rev]:
          print(string,'is a palindrome.')
          break
     else:
          print(string,'is not a palindrome.')

3. Find the largest/smallest number in a list/tuple
 
Download
# creating empty list 
list1 = [] 
  
# asking number of elements to put in list 
num = int(input("Enter number of elements in list: ")) 
  
# iterating till num to append elements in list 
for i in range(1, num + 1): 
    ele= int(input("Enter elements: ")) 
    list1.append(ele) 
      
# print maximum element 
print("Largest element is:", max(list1))

# print minimum element 
print("Smallest element is:", min(list1)) 
 

4. WAP to input any two tuples and swap their values.
 
Download
t1 = tuple()
n = int (input("Total no of values in First tuple: "))
for i in range(n):
     a = input("Enter Elements : ")
     t1 = t1 + (a,)
t2 = tuple()
m = int (input("Total no of values in Second tuple: "))
for i in range(m):
     a = input("Enter Elements : ")
     t2 = t2 + (a,)
print("First Tuple : ")
print(t1)
print("Second Tuple : ")
print(t2)

t1,t2 = t2, t1

print("After Swapping: ")
print("First Tuple : ")
print(t1)
print("Second Tuple : ")
print(t2)

5. WAP to store students’ details like admission number, roll number, name and percentage in a dictionary and display information on the basis of admission number.

 
Download
record = dict ()
i=1
n= int (input ("How many records u want to enter: "))
while(i<=n):
     Adm = input("Enter Admission number: ")
     roll = input("Enter Roll Number: ")
     name = input("Enter Name :")
     perc = float(input("Enter Percentage : "))
     t = (roll,name, perc)
     record[Adm] = t
     i = i + 1
Nkey = record.keys() 
for i in Nkey:
     print("\nAdmno- ", i, " :")
     r = record[i]
     print("Roll No\t", "Name\t", "Percentage\t")
     for j in r:
          print(j, end = "\t")

6. Write a program with a user-defined function with string as a parameter which replaces all vowels in the string with ‘*’.
 
Download
def strep(str):

# convert string into list

     str_lst =list(str) 

# Iterate list                         

     for i in range(len(str_lst)):

# Each Character Check with Vowels                

          if str_lst[i] in 'aeiouAEIOU':

# Replace ith position vowel with'*'          

               str_lst[i]='*'  

#to join the characters into a new string.                   

               new_str = "".join(str_lst)   
     return new_str

def main():
     line = input("Enter string: ")
     print("Orginal  String")
     print(line)
     print("After replacing Vowels with '*'")
     print(strep(line))
main()
 

7. Recursively find the factorial of a natural number.
 
Download
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
     n = int(input("Enter any number: "))
     print("The factorial of given number is: ",factorial(n))
main()
 

8. Write a recursive code to find the sum of all elements of a list.
 
Download
def lstSum(lst,n):
     if n==0:
          return 0
     else:
          return lst[n-1]+lstSum(lst,n-1)

mylst = [] # Empty List

#Loop to input in list

num = int(input("Enter how many number :"))
for i in range(num):
     n = int(input("Enter Element "+str(i+1)+":"))
     mylst.append(n) #Adding number to list
     sum = lstSum(myl
                  st,len(mylst))
print("Sum of List items ",mylst, " is :",sum)
 

9. Write a recursive code to compute the nth Fibonacci number.
 
Download
def fibonacci(n):
     if n == 0:
       return 0
     elif n == 1:
       return 1
     else:
       return(fibonacci(n-2) + fibonacci(n-1))

nterms = int(input("Please enter the Range Number: "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fibonacci(i),end='   ')
 

10.Read a text file line by line and display each word separated by a #.
 
Download
filein = open("Mydoc.txt",'r')
line =" "
while line:
     line = filein.readline()
     #print(line)
     for w in line:
          if w == ' ':
               print('#',end = '')
          else:
               print(w,end = '')
filein.close()


'''
#-------------OR------------------

filein = open("Mydoc.txt",'r')
for  line in filein:
     word= line .split()
     for w in word:
          print(w + '#',end ='')
     print()
filein.close()

'''
 

11. Read a text file and display the number of vowels/ consonants/ uppercase/ lowercase characters and other than character and digit in the file.
 
Download
filein = open("Mydoc1.txt",'r')
line = filein.read()
count_vow = 0
count_con = 0
count_low = 0
count_up = 0
count_digit = 0
count_other = 0
print(line)
for ch in line:
     if ch.isupper():
          count_up +=1
     if ch.islower():
          count_low += 1
     if ch in 'aeiouAEIOU':
          count_vow += 1
     if ch.isalpha():
          count_con += 1
     if ch.isdigit():
          count_digit += 1
     if not ch.isalnum() and ch !=' ' and ch !='\n':
          count_other += 1
          
print("Digits",count_digit)          
print("Vowels: ",count_vow)
print("Consonants: ",count_con-count_vow)
print("Upper Case: ",count_up)
print("Lower Case: ",count_low)
print("other than letters and digit: ",count_other)

filein.close()

12. Write a Python code to find the size of the file in bytes, the number of lines, number of words and no. of character.
 
Download
import os

lines = 0
words = 0
letters = 0
filesize = 0

for line in open("Mydoc.txt"):
    lines += 1
    letters += len(line)
    # get the size of file
    filesize = os.path.getsize("Mydoc.txt")
    
    # A flag that signals the location outside the word.
    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'

print("Size of File is",filesize,'bytes')
print("Lines:", lines)
print("Words:", words)
print("Letters:", letters)
 

13. Write a program that accepts a filename of a text file and reports the file's longest line.
 
Download
def get_longest_line(filename):
    large_line = ''
    large_line_len = 0

    with open(filename, 'r') as f:
        for line in f:
            if len(line) > large_line_len:
                large_line_len = len(line)
                large_line = line

    return large_line

filename = input('Enter text file Name: ')
print (get_longest_line(filename+".txt"))

14. Create a binary file with the name and roll number. Search for a given roll number and display the name, if not found display appropriate message.
 
Download
import pickle

def  Writerecord(sroll,sname):
    with open ('StudentRecord1.dat','ab') as Myfile:
        srecord={"SROLL":sroll,"SNAME":sname}        
        pickle.dump(srecord,Myfile)
       
def Readrecord():
    with open ('StudentRecord1.dat','rb') as Myfile:
        print("\n-------DISPALY STUDENTS DETAILS--------")
        print("\nRoll No.",' ','Name','\t',end='')
        print()
        while True:
           try:
               rec=pickle.load(Myfile)
               print(' ',rec['SROLL'],'\t  ' ,rec['SNAME'])
           except EOFError:
                break
def Input():
    n=int(input("How many records you want to create :"))
    for ctr in range(n):
        sroll=int(input("Enter Roll No: "))
        sname=input("Enter Name: ")
        Writerecord(sroll,sname)
        
def SearchRecord(roll):
    with open ('StudentRecord1.dat','rb') as Myfile:
       while True:
          try:
               rec=pickle.load(Myfile)
               if rec['SROLL']==roll:
                   print("Roll NO:",rec['SROLL'])
                   print("Name:",rec['SNAME'])

          except EOFError:
               print("Record not find..............")
               print("Try Again..............")
               break

def main():
   
    while True:
        print('\nYour Choices are: ')
        print('1.Insert Records')
        print('2.Dispaly Records') 
        print('3.Search Records (By Roll No)')
        print('0.Exit (Enter 0 to exit)')
        ch=int(input('Enter Your Choice: '))
        if ch==1:
            Input()
        elif ch==2:
            Readrecord()
        elif ch==3:
            r=int(input("Enter a Rollno to be Search: "))
            SearchRecord(r)
        else:
            break
main()

15. Create a binary file with roll number, name and marks. Input a roll number and update details.
 
Download
def  Writerecord(sroll,sname,sperc,sremark):
    with open ('StudentRecord.dat','ab') as Myfile:
        srecord={"SROLL":sroll,"SNAME":sname,"SPERC":sperc,
                 "SREMARKS":sremark}        
        pickle.dump(srecord,Myfile)
       
def Readrecord():
    with open ('StudentRecord.dat','rb') as Myfile:
        print("\n-------DISPALY STUDENTS DETAILS--------")
        print("\nRoll No.",' ','Name','\t',end='')
        print('Percetage',' ','Remarks')
        while True:
           try:
               rec=pickle.load(Myfile)
               print(' ',rec['SROLL'],'\t  ' ,rec['SNAME'],'\t ',end='')
               print(rec['SPERC'],'\t   ',rec['SREMARKS'])
           except EOFError:
                break
def Input():
    n=int(input("How many records you want to create :"))
    for ctr in range(n):
        sroll=int(input("Enter Roll No: "))
        sname=input("Enter Name: ")
        sperc=float(input("Enter Percentage: "))
        sremark=input("Enter Remark: ")
        Writerecord(sroll,sname,sperc,sremark)
        

def Modify(roll):
    with open ('StudentRecord.dat','rb') as Myfile:
        newRecord=[]
        while True:
           try:
               rec=pickle.load(Myfile)
               newRecord.append(rec)
           except EOFError:
                break
    found=1       
    for i in range(len(newRecord)):
        if newRecord[i]['SROLL']==roll:
            name=input("Enter Name: ")
            perc=float(input("Enter Percentage: "))
            remark=input("Enter Remark: ")

            newRecord[i]['SNAME']=name
            newRecord[i]['SPERC']=perc
            newRecord[i]['SREMARKS']=remark
            found =1
        else:
            found=0

    if found==0:

        print("Record not found")
    with open ('StudentRecord.dat','wb') as Myfile:
         for j in newRecord:
             pickle.dump(j,Myfile)


def main():
   
    while True:
        print('\nYour Choices are: ')
        print('1.Insert Records')
        print('2.Dispaly Records') 
        print('3.Update Records')
        print('0.Exit (Enter 0 to exit)')
        ch=int(input('Enter Your Choice: '))
        if ch==1:
            Input()
        elif ch==2:
            Readrecord()
        elif ch==3:
            r =int(input("Enter a Rollno to be update: "))
            Modify(r)
        else:
            break
main()

16. Remove all the lines that contain the character `a' in a file and write it to another file

 
Download
f1 = open("Mydoc.txt")
f2 = open("copyMydoc.txt","w")
for line in f1:
     if 'a' not in line:
          f2.write(line)
print('## File Copied Successfully! ##')
f1.close()
f2.close()

f2 = open("copyMydoc.txt","r")
print(f2.read())

17. Write a program to perform read and write operation onto a student.csv file having fields as roll number, name, stream and percentage.​

 
Download
import csv
with open('Student_Details.csv','w',newline='') as csvf:
     writecsv=csv.writer(csvf,delimiter=',')
     choice='y'
     while choice.lower()=='y':
          rl=int(input("Enter Roll No.: "))
          n=input("Enter Name: ")
          p=float(input("Enter Percentage: "))
          r=input("Enter Remarks: ")
          writecsv.writerow([rl,n,p,r])
          print(" Data saved in Student Details file..")
          choice=input("Want add more record(y/n).....")
          
with open('Student_Details.csv','r',newline='') as fileobject:
     readcsv=csv.reader(fileobject)
     for i in readcsv:
          print(i)

18. Program to search the record of a particular student from CSV file on the basis of inputted name.
 
Download
import csv

#input Roll number you want to search

number = input('Enter number to find: ')
found=0
#read csv, and split on "," the line

with open('Student_Details.csv') as f:
     csv_file = csv.reader(f, delimiter=",")
     #loop through csv list
     for row in csv_file:

     #if current rows index value (here 0) is equal to input, print that row
          if number ==row[0]:
              print (row)
              found=1
          else:
               found=0
if found==1:
     pass

else:
     print("Record Not found")

20. Write a program to create a library in python and import it in a program.
 
Download
#Let's create a package named Mypackage, using the following steps:
#• Create a new folder named NewApp in D drive (D:\NewApp)
#• Inside NewApp, create a subfolder with the name 'Mypackage'.
#• Create an empty __init__.py file in the Mypackage folder
#• Create modules Area.py and Calculator.py in Mypackage folder with following code


# Area.py Module

import math

def rectangle(s1,s2):
    area = s1*s2
    return area

def circle(r):
    area= math.pi*r*r
    return area

def square(s1):
     area = s1*s1
     return area

def triangle(s1,s2):
     area=0.5*s1*s2
     return area


# Calculator.py Module

def sum(n1,n2):
    s = n1 + n2
    return s

def sub(n1,n2):
    r = n1 - n2
    return r

def mult(n1,n2):
     m = n1*n1
     return m

def div(n1,n2):
     d=n1/n2
     return d


# main() function

from Mypackage import Area
from Mypackage import Calculator

def main():
     

     r = float(input("Enter Radius: "))
     area =Area.circle(r)
     print("The Area of Circle is:",area)

     s1 = float(input("Enter side1 of rectangle: "))
     s2 = float(input("Enter side2 of rectangle: "))
     area = Area.rectangle(s1,s2)
     print("The Area of Rectangle is:",area)      

     s1 = float(input("Enter side1 of triangle: "))
     s2 = float(input("Enter side2 of triangle: "))
     area = Area.triangle(s1,s2)
     print("The Area of TriRectangle is:",area)

     s = float(input("Enter side of square: "))
     area =Area.square(s)
     print("The Area of square is:",area)

     num1 = float(input("\nEnter First number :"))
     num2 = float(input("\nEnter second number :"))

     print("\nThe Sum is : ",Calculator.sum(num1,num2))

     print("\nThe Multiplication is : ",Calculator.mult(num1,num2))

     print("\nThe sub is : ",Calculator.sub(num1,num2))

     print("\nThe Division is : ",Calculator.div(num1,num2))

main()
 

21. Write a python program to implement sorting techniques based on user choice using a list data-structure. (bubble/insertion)
 
Download
#BUBBLE SORT FUNCTION
def Bubble_Sort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp


#INSERTION SORT FUNCTION

def Insertion_Sort(nlist):
   for index in range(1,len(nlist)):

     currentvalue = nlist[index]
     position = index

     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]
         position = position-1

     nlist[position]=currentvalue

 

# DRIVER CODE

def main():
    print ("SORT MENU")
    print ("1. BUBBLE SORT")
    print ("2. INSERTION SORT")
    print ("3. EXIT")
    choice=int(input("Enter your Choice [ 1 - 3 ]: "))
    nlist = [14,46,43,27,57,41,45,21,70]
    if choice==1:
        print("Before Sorting: ",nlist)
        Bubble_Sort(nlist)
        print("After Bubble Sort: ",nlist)
    elif choice==2:
        print("Before Sorting: ",nlist)
        Insertion_Sort(nlist)
        print("After Insertion Sort: ",nlist)
    else:
        print("Quitting.....!")

main()
 

22. Take a sample of ten phishing e-mails (or any text file) and find the most commonly occurring word(s).
 
Download

def Read_Email_File():
    import collections
    fin = open('email.txt','r')
    a= fin.read()
    d={ }
    L=a.lower().split()
    for word in L:
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("&","")
        word = word.replace("*","")
    for k in L:
        key=k
        if key not in d:
            count=L.count(key)
            d[key]=count
    n = int(input("How many most common words to print: "))
    print("\nOK. The {} most common words are as follows\n".format(n))
    word_counter = collections.Counter(d)
    for word, count in word_counter.most_common(n):
        print(word, ": ", count)
    fin.close()

#Driver Code
def main():
    Read_Email_File()
main()

23. Write a python program to implement a stack using a list data-structure.
 
Download

def isempty(stk):
    if stk==[]:
        return True
    else:
        return False

def push(stk,item):
    stk.append(item)
    top=len(stk)-1

def pop(stk):
    if isempty(stk):
        return "underflow"
    else:
        item=stk.pop()
    if len(stk)==0:
        top=None
    else:
        top=len(stk)-1
        return item

def peek(stk):
    if isempty(stk):
        return "underflow"
    else:
        top=len(stk)-1
        return stk[top]

def display(stk):
    if isempty(stk):
        print('stack is empty')
    else:
        top=len(stk)-1
        print(stk[top],'<-top')
        for i in range(top-1,-1,-1):
            print(stk[i])

#Driver Code
            
def main():    
    stk=[]
    top=None
    while True:
        print('''stack operation
                 1.push
                 2.pop
                 3.peek
                 4.display
                 5.exit''')
        choice=int (input('enter choice:'))
        if choice==1:
            item=int(input('enter item:'))
            push(stk,item)
        elif choice==2:
            item=pop(stk)
            if item=="underflow":
                print('stack is underflow')
            else:
                print('poped')
        elif choice==3:
            item=peek(stk)
            if item=="underflow":
                print('stack is underflow')
            else:
                print('top most item is:',item)
        elif choice==4:
            display(stk)
        elif choice==5:
            break
        else:
            print('invalid')
            exit()
main()
 

24. Write a program to implement a queue using a list data structure.
 
Download
# Function to check Queue is empty or not
def isEmpty(qLst):
     if len(qLst)==0:
          return 1
     else:
          return 0


# Function to add  elements in Queue
def Enqueue(qLst,val):
     qLst.append(val)
     if len(qLst)==1:
          front=rear=0
     else:
          rear=len(qLst)-1

# Function to Delete  elements in Queue
def Dqueue(qLst):
     if isEmpty(qLst):
          return "UnderFlow"
     else:
          val = qLst.pop(0)
     if len(qLst)==0:
          front=rear=None
     return val

# Function to Display top element of Queue
def Peek(qLst):
     if isEmpty(qLst):
          return "UnderFlow"
     else:
          front=0
          return qLst[front]

# Function to Display elements of Queue
def Display(qLst):
     if isEmpty(qLst):
          print("No Item to Dispay in Queue....")
     else:
          tp = len(qLst)-1
          print("[FRONT]",end=' ')
          front = 0
          i = front
          rear = len(qLst)-1
          while(i<=rear):
               print(qLst[i],'<-',end=' ')
               i += 1
          print()
          

# Driver function
def main():
     qList = []
     front = rear = 0
     while True:
          print()
          print("##### QUEUE OPERATION #####")
          print("1. ENQUEUE ")
          print("2. DEQUEUE ")
          print("3. PEEK ")
          print("4. DISPLAY ")
          print("0. EXIT ")
          choice = int(input("Enter Your Choice: "))
          if choice == 1:
               ele = int(input("Enter element to insert"))
               Enqueue(qList,ele)
          elif choice == 2:
               val = Dqueue(qList)
               if val == "UnderFlow":
                    print("Queue is Empty")
               else:
                    print("\n Deleted Element was : ",val)

          elif choice==3:
               val = Peek(qList)
               if val == "UnderFlow":
                    print("Queue is Empty")
               else:
                    print("Item at Front: ",val)

          elif choice==4:
               Display(qList)
          elif choice==0:
               print("Good Luck......")
               break

main()
                    

25. Write a python program to implement searching methods based on user choice using a list data-structure. (linear & binary)
 
Download
#Linear Search Function Definition
def Linear_Search( lst, srchItem): 
    found= False
    for i in range(len(lst)):
        if lst[i] == srchItem:
            found = True
            print(srchItem, ' was found in the list at index ', i)
            break
    if found == False:
        print(srchItem, ' was not found in the list!')

#Binary Search Definition

def binary_Search(Lst,num): 
  
    start = 0
    end = len(Lst) - 1
    mid = (start + end) // 2

    # We took found as False that is, initially
    # we are considering that the given number
    # is not present in the list unless proven

    found = False
    position = -1
    while start <= end:
         if Lst[mid] == num:
              found = True
              position = mid
              print('Number %d found at position %d'%(num, position+1))
              break
            
         if num > Lst[mid]:
                start = mid + 1
                mid = (start + end) // 2
         else:
                end = mid - 1
                mid = (start + end) // 2

    if found==False:
            print('Number %d not found' %num)

      
# DRIVER CODE
def main():
    print ("SEARCH MENU")
    print ("1. LINEAR SERACH")
    print ("2. BINARY SEARCH")
    print ("3. EXIT")
    choice=int(input("Enter your Choice [ 1 - 3 ]: "))
    arr = [12, 34, 54, 2, 3] 
    n = len(arr) 
    if choice==1:
        print("The List contains : ",arr)
        num=int(input("Enter number to be searched: "))
        index = Linear_Search(arr,num) 

    if choice==2:
        arr = [2, 3,12,34,54]  #Sorted Array
        print("The List contains : ",arr)
        num=int(input("Enter number to be searched: "))
        result = binary_Search(arr,num) 

main()








"""