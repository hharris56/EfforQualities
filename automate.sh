#!/bin/bash

# Hunter Harris
# Nov 16, 2020
# Automate the commandline work for running gestures.py


# if jsons directory exists remove it
if [[ -d "jsons/" ]]
then
	rm "jsons/" -r
fi
# create jsons directory
mkdir "jsons/"

# unzip files into jsons directory
for f in zips/*.zip
do
	# remove extension / path
	shorter="${f%%_*}"
	dirname=${shorter##zips/}
	echo -e "$f\t => \tjsons/$dirname"
	unzip -qq $f -d "jsons/$dirname"
	# move out of internal directory
	mv jsons/$dirname/TestOut/* "jsons/$dirname/"
	rm "jsons/$dirname/TestOut/" -r
done

# if imgs directory exists remove it
if [[ -d "imgs/" ]]
then
	rm "imgs/" -r
fi
# create imgs directory
mkdir "imgs/"
