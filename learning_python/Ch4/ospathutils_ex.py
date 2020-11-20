#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)

    # Check for item existence and type
    print("Item exists:", path.exists("joe.txt"))
    print("Item is a file:", path.isfile("joe.txt"))
    print("Item is a directory:", path.isdir("joe.txt"))

    # Work with file paths
    print("Item path:", path.realpath("joe.txt"))
    print("Item path and name:", path.split(path.realpath("joe.txt")))

    # Get the modification time
    t = time.ctime(path.getmtime("joe.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("joe.txt")))

    # Calculate how long ago the item was modified
    td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("joe.txt"))
    print ("It has been " + str(td) + " since the file was modified")
    print ("Or, " + str(td.total_seconds()) + " seconds")
  
if __name__ == "__main__":
    main()
