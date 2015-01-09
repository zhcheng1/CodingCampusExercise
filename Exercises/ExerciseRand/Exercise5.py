




import string
from random import choice
from random import randint


with open("text.txt", "a+") as file_1:
    for i in range(0, 10):
        s = ""
        for j in range(0, randint(0, 50)):
            strings = choice(string.letters)
            s += strings
        s += "\n"
        file_1.write(s)



with open("text.txt", "r") as file_2:
    k = 1
    for line in file_2:
        print "****** BEGIN RANDOM STRING %s******\n\n" %k

        letter_count = {}
        for letter in line:
            if letter != "\n":
                if letter not in letter_count.keys():
                    letter_count[letter] = 1
                else:
                    letter_count[letter] += 1


        for key in letter_count.keys():
            output = "%s" %key + " ==> " + "%s"%letter_count[key] + " "
            print output,

        print "\n\n*********************************\n\n"

        k += 1

open("text.txt", 'w').close()
