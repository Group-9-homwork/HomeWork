import os
import csv
import json
from Spider import *

class FileIO():
    def __init__(self):
        self.filePath = r'./data.csv'

    def readFile(self, path):
        if path:
            self.filePath = path
        # 判断文件是否存在。。。

        with open(self.filePath, "r") as f:
            for line in f.readlines():
                print(line)

    def writeFile(self, path, contents):
        if path:
            self.filePath = path
        print(self.filePath)

        with open(path, 'a+') as f:
            for content in contents:
                f.write(
                    f'{content.userName},{content.text}, {content.source}, {content.created_at}, {content.retweet_count},{content.reply_count}, {content.reward_count}, {content.fav_count}\n')
        return None

    def readJson(self):
        '''默认路径'''
        # 读取
        with open('./test_data.json', 'r') as f:  # 判断文件是否存在！！！或者不存在添加
            data = json.load(f)
            # print(type(data))  # dict
            return data

    def writeJson(self, dict):
        '''传入字典，使用默认路径'''
        # dict转化成json
        data = json.dumps(dict, indent=4)
        # 保存
        with open('./test_data.json', 'w') as f:
            f.write(data)
            # json.dump(data, f)