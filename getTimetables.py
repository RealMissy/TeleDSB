#!/usr/bin/env python
# -*- coding: utf-8 -*-

# requirements: https://github.com/jarrekk/imgkit

# how to run the script: python getTimetables.py -u USERNAME -p PASSWORD [-h]
 
from contextlib import contextmanager

import argparse
import urllib # for getting the DSB-API information
import json # for processing the DSB-API information
import imgkit # for converting the timetables from html to png
import time
import sys
import os

# parser setup
parser = argparse.ArgumentParser(description='TeleDSB', add_help=False)
parser.description = "Stop asking for help, here you have it !"

required = parser.add_argument_group('Required arguments')
required.add_argument('-u', '--username', required=True)
required.add_argument('-p', '--password', required=True)

optional = parser.add_argument_group('Optional arguments')
optional.add_argument("-h", "--help", action="help", help="show this help message and exit")
args = parser.parse_args()

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        sys.stderr = os.devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

def check_account(USERNAME,PASSWORD):
    url = "https://dsbclient.noim.io/%s/%s" % (USERNAME, PASSWORD)
    response = urllib.urlopen(url)
    dsbData = json.loads(response.read())
    if dsbData == {}:
        return False
    else:
        return True
    
USERNAME = args.username 
PASSWORD = args.password

while 1:
    if check_account(args.username, args.password) == True :
        print("Successfully logged in")
    else:
        print("The username or password you used is incorrect. Please check the credentials and try again")
        sys.exit()
        
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

    print("-----------please ignore the follering messages-----------")

    # conversion from html to .jpg
    with suppress_stdout():
        imgkit.from_url(str(timetableUrls[0]),'%s[0].jpg' % USERNAME)
        imgkit.from_url(str(timetableUrls[1]),'%s[1].jpg' % USERNAME)
        
    print("----------------------------------------------------------")
    
    # sleep for 30 Minutes (30*60Seconds = 1800 Seconds)
    print("waiting 30 minutes for next update")
    time.sleep(1800) # every 30 minutes the script gets the timetables