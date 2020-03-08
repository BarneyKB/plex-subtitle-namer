import os
import re

files = [f for f in os.listdir()]


subs = [(f,[int(i) for i in re.findall(r'\d+',re.findall(r's\d{1,2}e\d{1,2}',f.lower())[0])]) for f in files if f[-3:].lower() == "srt"]
videos = [(f,[int(i) for i in re.findall(r'\d+',re.findall(r's\d{1,2}e\d{1,2}',f.lower())[0])]) for f in files if f[-3:].lower() in ["mkv","mov","mp4"]]

for subName, subSE in subs:
    for vidName, vidSE in videos:
        if subSE == vidSE:
            os.rename(subName,str(vidName[:-3]+"srt"))