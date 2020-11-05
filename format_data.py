# Hunter Harris
# October 25th, 2020

# imports
import csv
import json
import os
import sys
import time

def main():
    eqDict = {'glide': [0,0,0,1]}
    # check args + get directory/file names
    dirpath = checkargs()
    eq = eqDict[sys.argv[2]]
    print("1: Directory located")
    dirname = sys.argv[1].strip('/')
    filelist = os.listdir(dirpath)

    # open csv
    try:
        with open("{}.csv".format(dirname), 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            print("2: {}.csv opened".format(dirname))

            # for each file in directory
            for i in range(len(filelist)):
                print('\r3: Formatting {}/{}'.format(i+1, len(filelist)), end='')
                
                # open file
                filename = "{}/{}".format(dirname, filelist[i])
                try:
                    with open(filename) as jfile:
                        # read from json file
                        try:
                            data = json.load(jfile)
                            posepoints = data['people'][0]['pose_keypoints_2d']
                            # write data to csv file
                            try:
                                csvwriter.writerow(posepoints)
                            except:
                                print("\nFailed to write data from '{}'... skipping".format(filename))
                        except:
                            print("\nFailed to read from '{}'... skipping".format(filename))
                except:
                    print("\nFailed to open '{}'... skipping".format(filename))
            csvwriter.writerow(eq)
            print("\n4: Written to {}.csv".format(dirname))
    except:
        print("Failed to open '{}'... exiting".format(dirname))
    

# check if user provided a valid local directory path
def checkargs():
    # ensure directory provided
    if len(sys.argv) < 3:
        print("Error: format_data requires a directory name containing video data and an effort quality")
        exit()
    # ensure path exists
    dataDir = "{}/{}".format(os.getcwd(), sys.argv[1])
    if not os.path.exists(dataDir):
        print("Error: the provide directory path does not exist")
        print("HINT: Ensure you are referencing the directory from the cwd")
        exit()
    # ensure path is a directory
    if not os.path.isdir(dataDir):
        print("Error: the provided path is not a directory")

    return dataDir

if __name__ == "__main__":
    main()
