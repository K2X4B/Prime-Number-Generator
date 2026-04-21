import re

def Main():
    while True:
        print("--------------------")
        n = int(input("Enter a number: "))
        print(not re.match(r'^.?$|^(..+?)\1+$', '1'*n))

if __name__ == "__main__":
    print("************************************")    
    print("Welcome to the Prime Number Checker!")
    print("************************************")
    Main()