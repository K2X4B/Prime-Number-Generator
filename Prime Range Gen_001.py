import re
import time

def Main():
    s = int(input("Start of Range: "))
    e = int(input("End of Range: "))
    n = s
    list = []
    while n <= e:
    
        if not re.match(r'^.?$|^(..+?)\1+$', '1'*n):
            print(n)
            list.append(n)
        n += 1
    print("**************************")
    print(len(list), "Prime Numbers Found!")
    print("**************************")

    print("Prime Numbers in Range: ")
    print(list)
  
    print("**************************")
    press = input("Press Enter to Exit...")
#        time.sleep(0.25)

if __name__ == "__main__":
    print("*************************")
    print("Prime Number Calculator")
    print("*************************")
    Main()
#42
