import requests
import re
from datetime import datetime
from dateutil.relativedelta import relativedelta

def splitList(listOfLinks, seperator):
    listSplit = listOfLinks.split(seperator)
    return listSplit

def findVideoID(realList):
    video_ids = []
    for video in realList:
        video = str(video)
        match = re.search(r'(?<=v=)[^&]+', video)
        if match:
            video_id = match.group(0)
            video_ids.append(video_id)
    return video_ids

listOfLinks = input("Enter list: ")
seperator = input("Enter seperator: ")
realList = splitList(listOfLinks, seperator)
listOfVideoIDs = findVideoID(realList)

months_difference = []

for ID in listOfVideoIDs:
    r= requests.get("https://www.googleapis.com/youtube/v3/videos?part=snippet&id=" + ID + "&key=AIzaSyCilxh2n7MBerAKLykKxzLd1qDci3gN0jg")
    response = r.json()
    for item in response["items"]:
        published_date = item['snippet']["publishedAt"]
        date_part = published_date.split("T")[0]
        published_date = datetime.strptime(date_part, "%Y-%m-%d")
        current_date = datetime.now()
        difference = relativedelta(current_date, published_date)
        months_difference.append(difference.years * 12 + difference.months)

for months in months_difference:
    print(str(months) + " months")
