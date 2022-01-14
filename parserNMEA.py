import sys
import re
from datetime import datetime

if __name__=="__main__":
    data = []
    try:
        fileToRead = open(sys.argv[1], "r")
        fileToWrite = open("parseNMEA " + sys.argv[1], "w")
        fileToWrite.write("Time Latitude N/S Longitude E/W qulity_indicator Satelites_used\n")
        
        for line in fileToRead:
            if re.search("GNGGA", line):
                x = re.split("\,", line[:-1])
                fileToWrite.write(x[1]+" "+x[2]+" "+x[3]+" "+x[4]+" "+x[5]+" "+x[6]+" "+x[7]+"\n")
                
        fileToWrite.close()
        fileToRead.close()
        print(data)
    except e:
        print(e)