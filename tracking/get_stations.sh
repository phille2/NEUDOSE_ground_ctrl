#!/bin/sh

URL_LINK="http://www.celestrak.com/NORAD/elements/stations.txt"
FILE_NAME="stations.txt"

wget $URL_LINK
sed -i -e 's/\s\+$//g' $FILE_NAME

