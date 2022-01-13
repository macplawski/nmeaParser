import sys
import re

if __name__=="__main__":
    print("blalba")
    try:
        file = open(sys.argv[1], "r")

        for line in file:
            x = re.split("\,", line[:-1])
            print(x)
    except e:
        print(e)