import sys
import time

if __name__ == '__main__':
    
    file_name=list(sys.argv)[1]
    f = open(file_name, "x")
    print("File ",file_name," created successfully")
    time.sleep(30)
    f.close()
    print("Terminating the program")
    