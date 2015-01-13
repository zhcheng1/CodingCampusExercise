
def converter_2():
    user_input = raw_input("Please enter a speed in miles/hour: ")
    while not user_input.isdigit():
        user_input = raw_input("Please enter an integer as a speed in miles/hour: ")

    return user_input


inmile = int(converter_2())
#convert to meter
inmeter = inmile * 1609.34
#convert to barley/day
inbarley = inmeter * 117.647 * 24
#convert to furlong/fortnight
infurlong = inmeter * 1.09361 / 220 * 24 * 7 * 2
#convert to Mach
inmach = inmeter * 3.28084 / 3600 / 1130.0
#convert to percent of speed of light
inlight = inmeter / 3600 / 299792458

print "Original speed in mph is: %.1f" %inmile
print "Converted to barleycorn/day is : %.3f" %inbarley
print "Converted to furlong/fortnight is : %.1f" %infurlong
print "Converted to Mach number is : %s" %inmach
print "Converted to the percentage of the speed of light is : %s" %inlight

