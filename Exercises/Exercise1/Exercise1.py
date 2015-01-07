

def get_input(input_count):
    user_input = raw_input("Please enter the " + input_count +" integer: ")
    while not user_input.isdigit() or (user_input == "0"):
        if input_count is not "first":
            if user_input == "0":
                user_input = raw_input("Please enter an integer besides 0:")
            else:
                user_input = raw_input( "Please enter an integer:")
        else:
            user_input = raw_input("Please enter an integer: ")
    return user_input

first = get_input("first")

second= get_input("second")

first_num = int(first)

second_num = int(second)


#print sum, subtraction, product, quotient
print "The sum of %s and %s is: " %(first, second), first_num + second_num
print "The difference of %s and %s is: " %(first, second), abs(first_num - second_num)
print "The product of %s and %s is: " %(first, second), first_num * second_num
print "The quotient of %s and %s is " %(first, second), first_num / second_num, " with remainder ", first_num % second_num



#check if the input is a number
while not first.isdigit():
    first = raw_input("Enter integers only. Please enter the first integer: ")

#transform the first input str into int
first_num = int(first)

#get the second number
second = raw_input("Please enter the second integer: ")

#check if the second input is a number or 0
while (not second.isdigit() or second == "0"):
    if second == "0":
        second = raw_input("Please do not enter 0 as divisor. Please enter the second integer: ")
    else:
        second = raw_input("Enter integers only. Please enter the second integer: ")

#transform the first input str into int
second_num = int(second)

#print sum, subtraction, product, quotient
print "The sum of %s and %s is: " %(first, second), first_num + second_num
print "The difference of %s and %s is: " %(first, second), abs(first_num - second_num)
print "The product of %s and %s is: " %(first, second), first_num * second_num
print "The quotient of %s and %s is " %(first, second), first_num / second_num, " with remainder ", first_num % second_num


