import os
import pandas as pd
from IPython.display import display

def main():
    data = []
    lines = open('/mnt/ramdisk/log_ckpt2.txt', 'r').readlines()

    w_locs = ["WRITE1", "WRITE2", "WRITE3", "WRITE4", "WRITE5", "WRITE6"]
    r_locs = ["READ1", "READ2", "READ3", "READ4", "READ5"]
    rd_locs = ["RD1", "RD2", "RD3", "RD4", "RD5", "RD6"]
    w_times = {}
    r_times = {}
    rd_times = {}
    for loc in w_locs:
        w_times[loc] = []
    for loc in r_locs:
        r_times[loc] = []
    for loc in rd_locs:
        rd_times[loc] = []
    for line in lines:
        loc_and_pairs = line.strip().split('|')
        pairs = loc_and_pairs[1].strip().split(',')
        time = float(pairs[0].split(':')[1])
        loc = loc_and_pairs[0]
        if loc in w_locs:
            w_times[loc].append(time)
        elif loc in r_locs:
            r_times[loc].append(time)
        else:
            rd_times[loc].append(time)
    
    for loc in w_locs:
        print(loc, sum(w_times[loc]))
    for loc in r_locs:
        print(loc, sum(r_times[loc]))
    for loc in rd_locs:
        print(loc, len(rd_times[loc]))
        print(loc, sum(rd_times[loc]))

       
    #df = pd.DataFrame(data=data)    
    #display(df)
    #df.to_csv('log/log.csv')

if __name__ == "__main__":
    main()
    

            
