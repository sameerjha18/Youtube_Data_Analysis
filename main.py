from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import csv

def configure():
    load_dotenv()


def apiConnection():
    youtube = build('youtube', 'v3', developerKey=os.getenv('api_key')) # Making Connection with api
    return youtube

def channeldetails(connection):
    data = []
    request = connection.search().list(
            part="snippet",
            type="video",
            q="FryingPanLIVEE",
            maxResults=50
    )
    response = request.execute()

    items = response.get('items')

    for x in items:
        id = x.get('id')
        snippet = x.get('snippet')
        details = {
            'videoId': id.get('videoId'),
            'channelId': snippet.get('channelId'),
            'title': snippet.get('title'),
            'description': snippet.get('description'),

        }
        data.append(details)
    return data
        
def videoData(connection,id):
    request = connection.videos().list(
        part="statistics",
        id=id
    )
    response = request.execute()
    
    items = response.get('items')

    for x in items:
        statistics = x.get('statistics')
        details = {
            'videoId': id,
            'viewCount': statistics.get('viewCount'),
            'likeCount': statistics.get('likeCount'),
            'commentCount': statistics.get('commentCount'),
        }
    return details

if __name__ == '__main__':
    configure()
    keys = channeldetails(apiConnection())[0].keys()
    with open('youtubeData.csv', 'w', encoding='utf-8', newline="") as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(channeldetails(apiConnection()))
    
    video_ids = [ sub['videoId'] for sub in channeldetails(apiConnection())]
    data = []
    for id in video_ids:
        data.append(videoData(apiConnection(), id))
    keys = data[0].keys()
    with open('videoData.csv', 'w', encoding='utf-8', newline="") as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    