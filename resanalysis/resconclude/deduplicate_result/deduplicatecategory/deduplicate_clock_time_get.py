import shutil

DIR = "./deduplicateresult"

def deduplicate_clock_time_get(filename):
    print(f"Deduplicating CLOCK_TIME_GETresult ...")
    outputfile = f"{DIR}/CLOCK_TIME_GET_final.txt"
    shutil.copy(filename, outputfile)
