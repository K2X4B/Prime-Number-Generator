import re
import time

def Main():
    n = 1
    while n > 0:
        if not re.match(r'^.?$|^(..+?)\1+$', '1'*n):
            print(n)
        n += 1
#        time.sleep(0.25)

if __name__ == "__main__":
    print("*************************")
    print("Prime Number Calculator")
    print("*************************")
    Main()
