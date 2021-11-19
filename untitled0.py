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

def vcul():
    f=open("Report.txt")
