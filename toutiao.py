import pymongo as pymongo
import requests

client = pymongo.MongoClient('localhost', 27017)
douban = client['douban']
musictop = douban['musictop']

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

url = ['https://music.douban.com/top250?start={}' .format(str(i)) for i in range(
        0
        ,
        250
        ,
        25
    )]

def get_url_music(url) :
    wb_data = requests.o