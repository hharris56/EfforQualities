# Hunter Harris
# Convert directory of JSON to images (with standard sizes)
# November 12th, 2020

import os
import glob
import numpy as np
import json
from PIL import Image

root = 'jsons/'
directories = ['push', 'float', 'punch', 'press', 
                'glide', 'slash', 'wring', 'dab', 'flick']

def main():
    minLen = get_min_dimensions()

    # make 'imgs' dir if it doesn't exist
    # if not os.path.isdir("imgs"):
    #     os.makedirs("imgs")
    # clear target directory
    # clear_directory("imgs")
    # ^^^ now handled in bash script

    # search for each label directory
    for label in directories:
        if os.path.isdir(root + label):
            print("directory: imgs/" + label)
            if not os.path.isdir("imgs/" + label):
                os.makedirs("imgs/" + label)
            # get each subdirectory
            # == get each video
            for direct in os.listdir(root + label):
                path = root + label + "/" + direct
                if os.path.isdir(path):
                    print(path + "\t=>\t", end="")
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
                    dirname = "/".join(path.split("/")[1:])
                    fp = "imgs/" + dirname + ".jpg"
                    img.save(fp)
                    print(fp)

def clear_directory(dirname):
    files = glob.glob(dirname + "/*")
    print("clearing: " + dirname)
    for f in files:
        # remove files from dir, then remove dir
        if os.path.isdir(f):
            clear_directory(f)
            os.rmdir(f)
        else:
            os.remove(f)

def normalize_array(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] / 1000
    return arr

def get_min_dimensions():
    minLength = int(99999)
    # search for each label directory
    for label in directories:
        if os.path.isdir(root + label):
            # count files in their subdirectories 
            # == count frames in each video
            for direct in os.listdir(root + label):
                path = root + label + "/" + direct
                if os.path.isdir(path):
                    minLength = min(minLength, len(os.listdir(path)))
    
    return minLength


if __name__ == "__main__":
    main()
