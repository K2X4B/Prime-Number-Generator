import re
import time
import random

def Main():
    n = 0
    stop = int(input("Stop at? : "))
    list = []
    while n <= stop:
        if not re.match(r'^.?$|^(..+?)\1+$', '1'*n):
            list.append(n)
            print(n)
        n += 1
#        time.sleep(0.25)
#    random.shuffle(list)

    print("**************************")
    shuffle = input("Shuffle? (y/n) : ")
    if shuffle == "y":
        random.shuffle(list)
        print("**************************")
        print("Shuffled Primes: ")
        print("**************************")
        print(list)
        print("**************************")
    else:
        print(list)
    again = input("Again? (y/n) : ")
    if again == "y":
        Main()
  
if __name__ == "__main__":
    print("**************************")
    print("Prime Number Calculator")
    print("**************************")
    Main()
