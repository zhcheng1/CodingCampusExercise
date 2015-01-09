
import string

s = ": ' --- oh, mighty king"


for i in s.split():
    if i.isalpha() == "False":
        i=" "

print s


