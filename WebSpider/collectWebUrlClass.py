import requests
import json
from bs4 import BeautifulSoup


class collectUrl():
    def __init__(self):
        self.base_url = 'http://xs.fzxs.com.cn'
        self.json_url = './url_data.json'
        self.arr = []
        self.data = {}

    def request(self, url):
        r = requests.get(url)
        return r

    def get_link(self, tag):
        return (tag.name == "img" and tag.has_attr('src')) or (tag.name == "script" and tag.has_attr('src')) or (tag.name == "link" and tag.has_attr('href')) or (tag.name == "a" and tag.has_attr('href'))

    def create_data(self, data, attr, obj):
        data = {'url': obj.get(attr)}
        self.arr.append(data)

    def save_data(self):
        print("开始保存文件")
        with open(self.json_url, 'w') as f:
            json_data = json.dumps(self.arr)
            f.write(json_data)
        print("保存完成，爬取结束")

    def collect_url(self):
        res = self.request(self.base_url)
        html = BeautifulSoup(res.text, 'lxml').find_all(self.get_link)
        for h in html:
            if h.name == "img" and h.has_attr('src'):
                self.create_data(self.data, 'src', h)
                # print('这是img标签', h)
            elif h.name == "script" and h.has_attr('src'):
                self.create_data(self.data, 'src', h)
                # print('这是script标签：', h)
            elif h.name == "link" and h.has_attr('href'):
                self.create_data(self.data, 'href', h)
                # print('这是link标签：', h)
            elif h.name == "a" and h.has_attr('href'):
                self.create_data(self.data, 'href', h)
                # print('这是a标签：', h)

        self.save_data()


colllect = collectUrl()
colllect.collect_url()
