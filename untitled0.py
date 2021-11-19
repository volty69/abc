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

"""def vcul():
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
