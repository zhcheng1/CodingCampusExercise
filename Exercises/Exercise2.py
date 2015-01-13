


def converter():
    user_input = raw_input("Please enter the number of gallons of gasoline: ")
    while not user_input.isdigit():
        user_input = raw_input("Please enter an integer for the number of gallons of gasoline: ")

    return user_input


user_input = int(converter())
num_gallons = int(user_input)
num_liters = num_gallons * 3.7854
num_barrel = num_gallons / 42
num_CO2 = num_gallons * 20
num_etho = 75700 / 11500 *  num_gallons
num_dollar = num_gallons * 4.00

print "Original number of gallons is: %.1f" %user_input
print "%.1f gallons of gasoline is equivalent of %.1f liters" %(user_input,num_liters)
print "%.1f gallons of gasoline requires %.1f barrels of oil" %(user_input,num_barrel)
print "%.1f gallons of gasoline produces %.1f ponds of CO2" %(user_input,num_CO2)
print "%.1f gallons of gasoline is energy to %.1f gallons of ethanol" %(user_input,num_etho)
print "%.1f gallons of gasoline requires %.1f US dollars" %(user_input,num_dollar)
print "Thanks for playing"