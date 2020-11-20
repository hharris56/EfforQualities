# Hunter Harris
# Looking at wrist values for openpose
# November 18, 2020

import os
import json
import numpy as np
import csv

wristIndex = 4
minLen = 60
effort_dict = {
    'float': 0,
    'punch': 1,
    'press': 0,
    'glide': 0,
    'slash': 1,
    'wring': 0,
    'dab': 1,
    'flick': 1
}

def main():

    output = []

    for labeldir in os.listdir('jsons'):
        print(labeldir)
        dirpath = 'jsons/' + labeldir
        for viddir in os.listdir(dirpath):
            print("\t" + viddir)
            vidpath = dirpath + '/' + viddir

            if len(os.listdir(vidpath)) > minLen:
                ind = 0
                wristPos = []

    
                for jfile in os.listdir(vidpath):
                    if ind < minLen:
                        jpath = vidpath + '/' + jfile
                        with open(jpath) as f:
                            data = json.load(f)
                            wristPos.append(data['people'][0]['pose_keypoints_2d'][wristIndex])
                        ind += 1
                    else:
                        break

                wristPos.append(effort_dict[labeldir])
                output.append(wristPos)
                print(np.array(wristPos))

    with open("output.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in output:
            csvwriter.writerow(row)
    
    return 0


if __name__ == "__main__":
    main()