import csv
from itertools import groupby
from collections import ChainMap
from _operator import itemgetter

def read_csv_file():
    video_views = []
    with open("videoData.csv", "r",) as file:
        data = csv.reader(file)
        header = next(data)
        for x in data:
            videoData = {
                "videoId": x[0],
                "view": x[1],
                "like": x[2],
                "comments": x[3]
            }
            video_views.append(videoData)
    return video_views

def readYoutubeData():
    video_data = []
    with open("youtubeData.csv", "r",) as file:
        data = csv.reader(file)
        header = next(data)
        for x in data:
            videoData = {
                "videoId": x[0],
                "channelId": x[1],
                "title": x[2],
                "description": x[3]
            }
            video_data.append(videoData)
    return video_data

def higest_views(views, n):
    sorted_data = sorted(views, key=lambda i: int(i['view']), reverse= True)
    topView = sorted_data[:n]
    return topView

def topvideoDetails(topview, youtubedata):
    dict_list = topview + youtubedata

    response = map(lambda dict_tuple: dict(ChainMap(*dict_tuple[1])), groupby(sorted(dict_list, key=lambda sub_dict: sub_dict["videoId"]), key=lambda sub_dict: sub_dict["videoId"]))
    
    return response

views_info = read_csv_file()
top_view =  higest_views(views_info, 3)
youtubeData = readYoutubeData()
topvideoDetails(top_view,youtubeData)