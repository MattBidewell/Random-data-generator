#!/usr/bin/python

# python generateData username,email,firstname,lastname,age 100
# command line input of what values you require via cmd arguments

import sys
import csv
import json
import random

FILE_NAME="dummy-data.csv"
ALPHA_NUMERIC="ABCDEFGHIJKLMNOPQRSTUVWYXZabcdefghijklmnopqrstuvwyxz123456789"
ARGS=sys.argv

def start(noOfLines):
    file = open(FILE_NAME, ("w+"))
    file.write("username,password,email,age\r\n")

    for i in range (0, noOfLines):
        data = generateData()
        file.write(data)

    file.close()

def generateData():
    name = generateName()
    username = generateUsername(name)
    password = generatePassword()
    email = generateEmail(name)
    age = generateAge()
    return username + "," + password + "," + email + "," + age + "\r\n"


def generatePassword():
    length=random.randint(8,25)
    password=""
    for i in range(0, length):
        password+=ALPHA_NUMERIC[random.randint(0,len(ALPHA_NUMERIC)-1)]
    return password

def generateAge():
    return str(random.randint(18,55))

def generateUsername(name):
    randomInt = random.randint(0,9999)
    return name + str(randomInt)

def generateEmail(name):
    emailDomains = readFile("domains.json")
    emailProvidors = readFile("emailProviders.json")
    randomInt = random.randint(0,100)
    return name + str(randomInt) + "@" + emailProvidors[random.randint(0, len(emailProvidors) -1)] + emailDomains[random.randint(0, len(emailDomains) -1)]

def generateName():
    nameData = readFile("names.json")
    return nameData[random.randint(0, len(nameData)-1)]

def readFile(filename):
    file = ""
    with open("./datasets/" + filename, "r") as f:
        for line in f:
            file += line
    return json.loads(file)

if(len(ARGS) != 2):
    print("Invalid Arguments \r\n Correct use: \npython generateData 100")
else:
    start(int(ARGS[1]))
