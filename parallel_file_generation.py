import sys
import os
import time
from multiprocessing import Pool

def create_file(file_name):    

    f = open(file_name, "x")
    print("File ",file_name," created by process ",os.getpid())
    time.sleep(5)
    f.close()

if __name__=="__main__":
    
    arg_len=len(sys.argv)
    num_proc=int(list(sys.argv)[arg_len-1])
    file_names=list(sys.argv)[1:arg_len-1]
    with Pool(processes=num_proc) as pool:
        pool.map(create_file,file_names)
    
        
    
