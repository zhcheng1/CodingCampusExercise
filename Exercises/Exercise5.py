
from random import choice
from random import randint
import string
#
#
# with open("text.txt", "a+") as file_1:
#     for i in range(0, 10):
#         s = ""
#         for j in range(1, randint(0, 50)):
#             strings = choice(string.letters)
#             s += strings
#         s += "\n"
#         file_1.write(s)
#
#
#
# with open("text.txt", "r") as file_2:
#     k = 1
#     for line in file_2:
#         print "****** BEGIN RANDOM STRING %s******\n\n" %k
#
#         letter_count = {}
#         for letter in line:
#             if letter != "\n":
#                 if letter not in letter_count.keys():
#                     letter_count[letter] = 1
#                 else:
#                     letter_count[letter] += 1
#
#
#         for key in letter_count.keys():
#             output = "%s" %key + " ==> " + "%s"%letter_count[key] + " "
#             print output,
#
#         print "\n\n*********************************\n\n"
#
#         k += 1
#
# open("text.txt", 'w').close()


import string
from operator import itemgetter


#build table for translating punctuations to spaces
punct = string.punctuation
space = " " * len(punct)
trantab = string.maketrans(punct, space)

#build a new dictionary
word_count = {}

#open a file
with open("test.txt", "r") as file_name:
#read line by line, break line into words
    for line in file_name:
        line = line.split()
#turn all words into lowercase, replace punctuations with spaces
        for word in line:
            word = word.lower()
            word = word.translate(trantab)
#count words
            if word not in word_count.keys():
                word_count[word] = 1
            else:
                word_count[word] += 1

#sort the word_count dictionary by values
sorted_word_count = sorted(word_count.items(), key=itemgetter(1), reverse=True)

#print word:count pairs
for item in sorted_word_count:
    print "%r : %s" %(item[0], item[1])



