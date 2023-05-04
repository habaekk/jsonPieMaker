import json
from tqdm import tqdm
import time

import lunDayQuery


# {"month": "00", "day": "00", "year": "00", "lunDay": "00", "moonPhase": "0"} 
# moonPhase: 1-firstQuarter, 2-fullMoon, 3-lastQuarter, 4-newMoon

# create a list of dictionaries

my_data = []

lunDayQuery = lunDayQuery.LunDayQuery()

iterY = range(2020, 2031)
iterM = range(1, 13)
iterD = range(1, 32)

for y in tqdm(iterY, total = len(iterY), desc = 'Year', ncols = 120, ascii = ' =', leave = True):    
    for m in tqdm(iterM, total = len(iterM), desc = 'Month', ncols = 120, ascii = ' =', leave = False): 
        for d in tqdm(iterD, total = len(iterD), desc = 'Day', ncols = 120, ascii = ' =', leave = False): 
            time.sleep(0.1)
            lunDay = lunDayQuery.fetchLunDay(str(m), str(d), str(y))
            if lunDay == -1:
                continue
            moonPhase = "0"
            if lunDay == "01":
                moonPhase = "1"
            elif lunDay == "07":
                moonPhase = "2"
            elif lunDay == "15":
                moonPhase = "3"
            elif lunDay == "22":
                moonPhase = "4"
            my_data.append({"month": str(m), "day": str(d), "year": str(y), "lunDay": str(int(lunDay)), "moonPhase": moonPhase})

print(my_data)

# convert the data to JSON
json_data = json.dumps(my_data)

# save the JSON to a file
with open("./my_file.json", "w") as f:
    f.write(json_data)
