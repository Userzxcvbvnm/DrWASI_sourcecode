import sys
import os
import time
sys.path.append("../funcparmutate")

from parmu_clock_res_get import parmu_clock_res_get

if __name__ == "__main__":
    start_time = time.time()
    
    
    directory = os.path.abspath("../funcparmutate")
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            filepath = os.path.join(directory, filename)
            print(f"************** Executing {filepath} ... **************")
            os.system(f"python {filepath}")
            print(f"\n\n\n\n\n")

    
    
    end_time = time.time()
    execution_time = end_time - start_time  
    print(f"Execution Time for Generating Test Cases: {execution_time:.2f} s")  