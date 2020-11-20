#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes 
    now = datetime.now()

    #### Date Formatting ####

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("Current year is %Y %y"))
    print(now.strftime("Current week is %A %a"))
    print(now.strftime("Current month is %B %b"))
    print(now.strftime("Current day is %d"))
    print(now.strftime("%a, %d %B, %y"))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Time and Date: %c"))
    print(now.strftime("Date: %x"))
    print(now.strftime("Time: %X"))

    #### Time Formatting ####

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current Time: %I:%M:%S %p"))
    print(now.strftime("Current Time: %H:%M:%S %p"))
 
if __name__ == "__main__":
  main();
