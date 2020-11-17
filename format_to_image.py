# Hunter Harris
# Convert directory of JSON to images (with standard sizes)
# November 12th, 2020

import os
import numpy as np
import json
from PIL import Image

directories = ['push', 'float', 'punch', 'press', 
                'glide', 'slash', 'wring', 'dab', 'flick']

def main():
    minLen = get_min_dimensions()

    if not os.path.isdir("imgs"):
        os.makedirs("imgs")

    # search for each label directory
    for label in directories:
        if os.path.isdir(label):
            if not os.path.isdir("imgs/" + label):
                os.makedirs("imgs/" + label)
            # get each subdirectory
            # == get each video
            for direct in os.listdir(label):
                path = label + "/" + direct
                if os.path.isdir(path):
                    arr = []
                    # read data from each json
                    # == read data from each frame
                    for filename in os.listdir(path):
                        filepath = path + "/" + filename
                        with open(filepath) as jfile:
                            data = json.load(jfile)
                            posepoints = data['people'][0]['pose_keypoints_2d']
                            arr.append(normalize_array(posepoints))
                        if len(arr) == minLen:
                            break
                    # format list into image
                    nparr = np.array(arr)
                    img = Image.fromarray(np.uint8(nparr * 255), 'L')
                    fp = "imgs/" + path + ".jpg"
                    img.save(fp)

def normalize_array(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] / 1000
    return arr

def get_min_dimensions():
    minLength = int(99999)
    # search for each label directory
    for label in directories:
        print(label)
        if os.path.isdir(label):
            # count files in their subdirectories 
            # == count frames in each video
            for direct in os.listdir(label):
                path = label + "/" + direct
                if os.path.isdir(path):
                    minLength = min(minLength, len(os.listdir(path)))
    
    return minLength


if __name__ == "__main__":
    main()