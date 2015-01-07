

user_input = raw_input("Please enter a speed in miles/hour: ")

inmile = int(user_input)
inmeter = inmile * 1609.34
inbarley = inmeter / 117.647


print "Original speed in mph is: %.1f" %inmile
