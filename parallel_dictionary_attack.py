import md5
import os
import sys
import multiprocessing

def getListPassword():
    counter = 0
    pwfile = raw_input("Enter a dictionary file: ")

    try:
        pwfile = open(pwfile, "r")
    except:
        print "\nFile Not Found"
        quit()

    listpw = []
    for password in pwfile:
        counter += 1
        pswrd = password.strip()
        listpw.append(pswrd)
    return listpw

pwlist = []
pwlist = getListPassword()
print len(pwlist)
