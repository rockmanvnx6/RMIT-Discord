import os
import datetime

txt_files = [f for f in os.listdir('.') if f.endswith('.ics')]
if len(txt_files) != 1:
    raise ValueError('should be only one txt file in the current directory')

filename = txt_files[0]

today = str(datetime.date.today())
date = datetime.datetime.strptime(today,"%Y-%m-%d")
today = date.strftime("%Y%m%d")

with open(filename,"r") as file:
    found = False
    subject = ""
    start = ""
    end = ""
    location = ""
    for i in file:
        target  = i.split(":")
        # if(target[0].startswith("SUMMARY")): #subject
        #     print(target[1].split("\\,")[0])
        # if(target[0].startswith("LOCATION")): #location
        #     print(target[1])
        # if(target[0].startswith("DTSTART")): #date
        #     print(target[1].split("T"))
        # if(target[0].startswith("DTEND")): #date
        #     print(target[1].split("T"))

        if(target[0].startswith("DTSTART")):
            time = target[1].split("T")
            if(time[0] == today):
                found = True
                start = time[1][:-1]
        if(found == True):
            if (target[0].startswith("DTEND")):  # date
                time = target[1].split("T")
                end = time[1][:-1]

            if (target[0].startswith("SUMMARY")):
                subject = target[1].split("\\,")[0]

            if (target[0].startswith("LOCATION")):
                location = target[1]
                print("Today you have: " + subject + " from " + start + " to " + end + " at: " + location)
                found = False