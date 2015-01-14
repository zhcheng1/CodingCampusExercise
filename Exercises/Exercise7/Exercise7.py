
#turn Celsius to Fahrenheit
def c2f (temperature):
    f = temperature * 1.8 + 32
    return int(f)


#turn Fahrenheit to Celsius
def f2c (temperature):
    c =  (temperature - 32) / 1.8
    return int(c)