import os
import csv
import json
from Spider import *
import pandas as pd


class FileIO():
    def __init__(self):
        self.filePath = './data.csv'
        self.jsonPath = './test_data.json'

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

        tmp = []
        for content in contents:
            tmp.append(content)

            '''with open(path, 'a+') as f:
                for content in contents:
                    # f.write( f'{content.userName},{content.text}, {content.source}, {content.created_at}, {content.retweet_count},{content.reply_count}, {content.reward_count}, {content.fav_count}\n')
                    f.write( f'{content.text}\n')'''
            return None

    def readCsv(self, path):
        '''读取csv转为字典'''
        commentData = pd.read_csv(path)
        commentData.set_index('ID').T.to_dict('list')
        pass

    def writeCsv(self, path, dataDict):
        '''把字典写入csv'''
        print(path)
        # 将数据转化为dataframe
        newData = pd.DataFrame(dataDict)
        print(newData)

        # 添加标签类
        labelClassDict = self.readJson()
        for labelClass in labelClassDict.keys():
            if labelClass not in newData.columns.values.tolist():
                newData[labelClass] = '待标注'

        # 读取原有数据
        if not os.path.exists(path):
            oldData = pd.DataFrame()
        else:
            oldData = pd.read_csv(path)
        print(oldData)

        # 合并数据
        data = pd.concat([oldData, newData])

        # 覆盖写回
        data.to_csv(path, index=None)

    def readJson(self):
        '''读取json文件'''
        # 读取
        with open('./test_data.json', 'r') as f:  # 判断文件是否存在！！！或者不存在添加
            data = json.load(f)
            # print(type(data))  # dict
            return data

    def writeJson(self, dict):
        '''写入json文件'''
        # dict转化成json
        data = json.dumps(dict, indent=4)
        # 保存
        with open('./test_data.json', 'w') as f:
            f.write(data)
            # json.dump(data, f)