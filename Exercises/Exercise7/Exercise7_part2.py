
import Exercise7

#cities and temperature waited to be converted
cities = {"Boston": "0 C", "Boise": "48 F", "Phoenix": "85 F", "Miami": "40 C",
          "Riverside": "30 C", "Baltimore": "32 F"
          }



def temperature_converter(dict):
#first identify the original temperature's format, then translate to another
#put the original value and converted value in a new dictionary
#with the order of (Celsius, Fahrenheit)

    for key, value in dict.items():

        #split the value into temperature and string
        value = value.split()

        #turn the original value to integer
        origin = int(value[0])

        #if the format is in Celsius, split the string and convert the value
        if value[1] == "C":
            converted = Exercise7.c2f(origin)
            dict[key] = (origin, converted)

        #if the format is in Fahrenheit
        elif value[1] == "F":
            converted = Exercise7.f2c(origin)
            dict[key] = (converted, origin)

    #print out the results
    for key, value in dict.items():
        print """In %s it is %s degrees Celsius,
    which is equivalent to %s degrees in Fahrenheit\n""" %(key, value[0], value[1])


temperature_converter(cities)


