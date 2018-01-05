#!/usr/bin/python3

# @author liu-feng
# @email w710989327@foxmail.com
# @time 2018/1/5 16:08
from html.parser import HTMLParser

__author__ = 'liu-feng'
__email__ = 'w710989327@foxmail.com'


class THTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        # print(data)
        pass

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


with open('../resource/python-example.html', 'r', encoding='utf-8') as f:
    data = f.read()
    parser = THTMLParser()
    parser.feed(data)
