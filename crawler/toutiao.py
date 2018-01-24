#!/usr/bin/python3

# @author liu-feng
# @email w710989327@foxmail.com
# @time 2018/1/24 14:49
import json
import os
import re
from _md5 import md5
from json import JSONDecodeError
from multiprocessing.pool import Pool
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup

__author__ = 'liu-feng'
__email__ = 'w710989327@foxmail.com'

MONGO_URL = 'localhost'
MONGO_DB = 'toutiao'
MONGO_TABLE = 'toutiao'

GROUP_START = 1
GROUP_END = 20
KEWORD = '街拍'


# ----------------------

# client = pymongo.MongoClient(MONGO_URL, connect=False)
# db = client[MONGO_DB]


def get_page_index(offset, keyword):
    data = {
        'autoload': 'true',
        'count': 20,
        'cur_tab': 3,
        'format': 'json',
        'keyword': keyword,
        'offset': offset
    }
    params = urlencode(data)
    base = 'http://www.toutiao.com/search_content/'
    url = base + '?' + params
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('Error occurred')
        return None
    pass


def download_image(url):
    print('Downloading: ', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)
        return None
        pass
    except ConnectionError:
        return None
    pass


def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    print(file_path)
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()
    pass


def parser_page_index(text):
    try:
        data = json.loads(text)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
        pass
    except JSONDecodeError:
        pass
    pass


def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None
    pass


def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    result = soup.select('title')
    title = result[0].get_text() if result else ''
    image_pattern = re.compile('gallery: JSON.parse\("(.*)"\)', re.S)
    result = re.search(image_pattern, html)
    if result:
        data = json.loads(result.group(1).replace('\\', ''))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images: download_image(image)
            return {
                'title': title,
                'url': url,
                'images': images
            }
    pass


# def save_to_mongo(result):
#     if db[MONGO_TABLE].insert(result):
#         print('Successfully Saved to Mongo', result)
#         return True
#     return False
#     pass


def main(offset):
    text = get_page_index(offset, keyword=KEWORD)
    urls = parser_page_index(text)
    for url in urls:
        html = get_page_detail(url)
        result = parse_page_detail(html, url)
        if result: print("保存成功")
    pass


if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
