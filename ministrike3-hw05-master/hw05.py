#!/usr/bin/python3
#
# In the space below, write a Python program.
#
# The program should prompt the user with the following message:
# "Please enter an integer representing a number of seconds: "
#
# The program should then print a message
#   converting the specified number of seconds into Weeks, Days, Hours, Minutes, and Seconds.
#
# For example, if the user runs the program and, when prompted, enters 917837, the result should be:
# weeks= 1 days= 3 hours= 14 minutes= 57 seconds= 17

seconds_input = int(input("Please enter an integer representing a number of seconds: "))
weeks=int(divmod(seconds_input,86400*7)[0])
days=int(divmod(seconds_input-(86400*7*weeks),86400)[0])
hours=int(divmod(seconds_input-(86400*7*weeks+86400*days),86400/24)[0])
minutes=int(divmod(seconds_input-(86400*7*weeks+86400*days+86400/24*hours),86400/(24*60))[0])
seconds=int(divmod(seconds_input-(86400*7*weeks+86400*days+86400/24*hours+86400/(24*60)*minutes),86400/(24*60*60))[0])
print('weeks= '+ str(weeks)+' days= '+ str(days) +' hours= '+ str(hours)+' minutes= ' + str(minutes)+' seconds= ' + str(seconds))
