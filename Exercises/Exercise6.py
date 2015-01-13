

def open_file(filename):
    open(filename, "r")
    print "I opened a file"


try:
    open_file("exercise6.txt")
except IOError as e:
    print "This file does not exist", type(e)


def open_file_other(filename):
    try:
        open(filename, "r")
        print "I opened a file"
    except IOError:
        print "file does not exist"


open_file_other("exercise5_2")