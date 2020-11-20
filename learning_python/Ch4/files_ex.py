#
# Read and write files using the built-in Python file methods
#

def main():  

    # Open a file for writing and create it if it doesn't exist
    f = open("joe.txt","w+")

    # write some lines of data to the file
    for i in range(10):
        f.write("Count" + str(i) + "\n")

    # close the file when done
    f.close()

   # Open the file for appending text to the end
    f = open("joe.txt","a")

    # write some lines of data to the file
    for i in range(100, 111):
        f.write("Count" + str(i) + "\n")

    # close the file when done
    f.close()

    # Open the file back up and read the contents
    f = open("joe.txt","r")

    if f.mode == 'r':
        contents = f.read()
        print(contents)
        
    f.close()

    f = open("joe.txt","r")

    if f.mode == 'r':        
        fl = f.readlines()
        for x in fl:
            print(x)

if __name__ == "__main__":
  main()
