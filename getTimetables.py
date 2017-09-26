#!/usr/bin/env python
# -*- coding: utf-8 -*-

# requirements: https://github.com/jarrekk/imgkit

# how to run the script: python getTimetables.py <<YOUR-DSB-USERNAME>> <<YOUR-DSB-PASSWORD>>

import urllib # for getting the DSB-API information
import json # for processing the DSB-API information
import imgkit # for converting the timetables from html to png
import time
import sys

USERNAME = sys.argv[1] # the first parameter after the file name
PASSWORD = sys.argv[2] # the second parameter after the filename

while 1:

    url = "https://dsbclient.noim.io/%s/%s" % (USERNAME, PASSWORD) # generate the url for the DSB-API
    response = urllib.urlopen(url) # raw input data
    dsbData = json.loads(response.read()) # unprocessed JSON data

    # initialize the arrays
    timetables = [0, 0] # it contains the timetables
    timetableUrls = ["", ""] # it contains the url to the corresponding timetable
    timetablesJpg = [0, 0] # it contains the JPG versions of the timetables

    # fill the arrays
    timetables[0] = dsbData['timetables'][0] # select the 1st timetable
    timetables[1] = dsbData['timetables'][1] # select the 2nd timetable

    timetableUrls[0] = dsbData['timetables'][0]['src'] # select the 1st timetable-Url
    timetableUrls[1] = dsbData['timetables'][1]['src'] # select the 2nd timetable-Url

    # conversion from html to .jpg
    imgkit.from_url(str(timetableUrls[0]),'%s[0].jpg' % USERNAME)
    imgkit.from_url(str(timetableUrls[1]),'%s[1].jpg' % USERNAME)

    # sleep for 30 Minutes (30*60Seconds = 1800 Seconds)
    print("waiting 30 Minutes")
    time.sleep(1800) # every 30 minutes the script gets the timetables
