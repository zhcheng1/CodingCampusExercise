
#show user menu get an input number
def exercisemenu ():
    print """
**********************
  Exercise 4 - Menu
**********************
1. Write input to file
2. Write input to screen
3. Quit
***********************"""
    user_input_num = raw_input("Enter your choice [1-3] : ")
    return user_input_num



#run the program until user chooses to quit
def choice():
    while True:
        input_num = exercisemenu ()

        #enter 1, write the input in a file
        if input_num == "1":
            line = raw_input("Enter a phrase: ")
            print "Writing " + line
            with open("text", "w") as file_1:
                file_1.write(line)
            exercisemenu ()

        #enter 2, print the line
        elif input_num == "2":
            line = raw_input("Enter a phrase: ")
            print "you entered: %r" %line
            exercisemenu ()

        #enter 3, quit the program
        elif input_num == "3":
            exit()

        #enter 4, give a hint and go back to menu
        else:
            print "you can only enter 1, 2, 3. "
            exercisemenu ()


choice()


