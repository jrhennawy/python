#
# Example file for working with classes
#

class myClass():
    def method1(self):
        print("myClass Method1")
    
    def method2(self, someString):
        print("myClass Method2", someString)

class childClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("childClass Method1")
    
    def method2(self, someString):
        print("childClass Method2")

def main():

    c = myClass()
    c.method1()
    c.method2("This is a String")

    c2 = childClass()

    c2.method1()
    c2.method2("This is a another String")


if __name__ == "__main__":
    main()
