#
# Example file for working with date information
#

from datetime import date 
from datetime import time
from datetime import datetime 

def main():
    ## DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    print("Today's date is:",date.today())

    # print out the date's individual components
    today = date.today()
    print("Today's date is:",today.day,today.month,today.year)

    # retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's weekday # is:",today.weekday())
    days = ["mon","tue","wed","thu","fri","sat","sun"]
    print("Which is a:",days[today.weekday()])

    ## DATETIME OBJECTS
    # Get today's date from the datetime class
    this_moment = datetime.now()
    print("Today's date & time is:",this_moment)

    # Get the current time
    now = datetime.time(datetime.now())
    print("Today's time is:",now)
  
if __name__ == "__main__":
  main();
  