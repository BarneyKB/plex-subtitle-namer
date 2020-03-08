import os
import re

# gets list of all files in the directory in which the program is being run
files = [f for f in os.listdir()]

# creates list of subtitle files (anything ending in "srt"), and also finds the episode and series number. Item format: ["filename", [int(seriesNumber), int(episodeNumber)]
subs = [(f, [int(i) for i in re.findall(r'\d+', re.findall(r's\d{1,2}e\d{1,2}', f.lower())[0])]) for f in files if f[-3:].lower() == "srt"]

# creates list of video files (anything ending in "mkv", "mov" or "mp4"), and also finds the episode and series number. Item format: ["filename", [int(seriesNumber), int(episodeNumber)]
videos = [(f, [int(i) for i in re.findall(r'\d+', re.findall(r's\d{1,2}e\d{1,2}', f.lower())[0])]) for f in files if f[-3:].lower() in ["mkv", "mov", "mp4"]]

# loops through all subtitle files
for subName, subSE in subs:
    for vidName, vidSE in videos:
        # if there is a video file with matching series and episode, rename the subtitle file to have the same name (except extension)
        if subSE == vidSE:
            os.rename(subName, str(vidName[:-3] + "srt"))
