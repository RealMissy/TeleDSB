#!/usr/bin/env python
# -*- coding: utf-8 -*-

# requirements: https://github.com/nickoala/telepot

import sys
import time
import telepot # responsible for handling the bot-api stuff
from telepot.loop import MessageLoop


def handleDsbAPI(msg, chat_id):
    msgText = msg['text'] # extract the messagetext from the raw message

    timetablesJpg = [0, 0] # it contains the JPG versions of the timetables


    if msgText == "%s, %s" % (USERNAME, PASSWORD): # just send the results, if there are any

        bot.sendChatAction(chat_id, "upload_photo") # to indicate the user something is happening

        timetablesJpg[0] = open("%s[0].jpg" % USERNAME, "r") # load the 1st timetable into a variable
        timetablesJpg[1] = open("%s[1].jpg" % USERNAME, "r") # load the 2nd timetable into a variable

        bot.sendPhoto(chat_id, timetablesJpg[0]) # send the user the 1st timetable

        bot.sendChatAction(chat_id, "upload_photo") # for completeness

        bot.sendPhoto(chat_id, timetablesJpg[1]) # send the user the 2nd timetable

        timetablesJpg[0].close() # free rescources by unloading the file
        timetablesJpg[1].close() # free rescources by unloading the file

    else:
        bot.sendMessage(chat_id, u"Die Zugangsdaten sind falsch, oder du hast das falsche Format angegeben, richtig wäre: <Nutzername>, <Passwort>")

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg) # extracting from the raw JSON-message
    msgText = msg['text'] # extract the messagetext from the raw message
    fromFirstName = msg['from']['first_name'] # extract the first name of the user
    print("content_type, chat_type, chat_id, msgText, fromFirstName") # debugging
    print(content_type, chat_type, chat_id, msgText, fromFirstName) # debugging

    if content_type == 'text':
        handleDsbAPI(msg, chat_id) # this function is sending messages on it's own



TOKEN = sys.argv[1]  # get token from command-line

USERNAME = sys.argv[2] # get DSB-USERNAME from command-line
PASSWORD = sys.argv[3] # get DSB-PASSWORD from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
