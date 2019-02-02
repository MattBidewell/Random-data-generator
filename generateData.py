#!/usr/bin/python

# python generateData username,email,firstname,lastname,age 100
# command line input of what values you require via cmd arguments

import sys
import csv
import random

FILE_NAME="dummy-data.csv"
ALPHA_NUMERIC="ABCDEFGHIJKLMNOPQRSTUVWYXZabcdefghijklmnopqrstuvwyxz123456789"
ARGS=sys.argv

def start(noOfLines):
    file = open(FILE_NAME, ("w+"))
    file.write("username,password,email,firstname,lastname,age\r\n")

    for i in range (0, noOfLines):
        data = generateData()
        file.write(data)

    file.close()

def generateData():
    username = generateUsername()
    password = generatePassword()
    email = generateEmail()
    age = generateAge()
    return "matt1402," + password + ",matt@test.com," + age + "\r\n"


def generatePassword():
    length=random.randint(8,25)
    password=""
    for i in range(0, length):
        password+=ALPHA_NUMERIC[random.randint(0,len(ALPHA_NUMERIC)-1)]
    return password

def generateAge():
    return str(random.randint(18,55))

def generateUsername():
    return "test"

def generateEmail():
    return "test@test.com"

if(len(ARGS) != 2):
    print("Invalid Arguments \r\n Correct use: \npython generateData 100")
else:
    start(int(ARGS[1]))
