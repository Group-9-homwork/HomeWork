# from code.Spider import *
import pandas as pd
import os
import json

class FileIO():
    def __init__(self):
        self.jsonPath = os.getcwd() + '\\LabelClass.json'
        print(self.jsonPath)

    '''def readFile(self, path):
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

            # with open(path, 'a+') as f:
                for content in contents:
                    # f.write( f'{content.userName},{content.text}, {content.source}, {content.created_at}, {content.retweet_count},{content.reply_count}, {content.reward_count}, {content.fav_count}\n')
                    f.write( f'{content.text}\n')
            return None'''

    def readCsv(self, path):
        '''读取csv转为字典'''
        #print(path)
        # 读取标签数据
        labelClassDict = self.readJson()

        # 读取原有数据
        try:
            oldData = pd.read_csv(path)
        except pd.errors.EmptyDataError:  # 如果数据是空的话，则添加列名
            colLabel = ['时间', '评论'] + list(labelClassDict.keys())
            oldData = pd.DataFrame(columns=colLabel)

        # if not os.path.exists(path):
        # else:
        #    oldData = pd.read_csv(path)
        #print(oldData)

        # 针对原有数据，对修改后的标签进行添加
        for labelClass in labelClassDict.keys():
            #print(labelClass)
            #print(oldData.columns.values.tolist())
            if labelClass not in oldData.columns.values.tolist():
                oldData[labelClass] = '待标注'
        # 覆盖写回
        oldData.to_csv(path, index=None)

        return oldData

    def writeCsv(self, path, dataDict):
        '''把字典写入csv'''
        #print(path)
        # 将数据转化为dataframe
        newData = pd.DataFrame(dataDict)
        #print(newData)

        # 读取标签数据
        labelClassDict = self.readJson()

        # 读取原有数据
        if not os.path.exists(path):
            oldData = pd.DataFrame()
        else:
            oldData = pd.read_csv(path)
        #print(oldData)

        # 针对原有数据，对修改后的标签进行添加
        for labelClass in labelClassDict.keys():
            if labelClass not in oldData.columns.values.tolist():
                oldData[labelClass] = '待标注'

        # 对新爬取的数据添加列，根据修改后的原有数据添加
        for labelClass in oldData.columns.values.tolist():
            if labelClass not in newData.columns.values.tolist():
                newData[labelClass] = '待标注'

        # 合并数据
        data = pd.concat([oldData, newData])

        # 覆盖写回
        data.to_csv(path, index=None)

    def readJson(self):
        '''读取json文件'''
        # 读取
        with open(self.jsonPath, 'r') as f:  # 判断文件是否存在！！！或者不存在添加
            data = json.load(f)
            # print(type(data))  # dict
            return data

    def writeJson(self, dict):
        '''写入json文件'''
        # dict转化成json
        data = json.dumps(dict, indent=4)
        # 保存
        with open(self.jsonPath, 'w') as f:
            f.write(data)
            # json.dump(data, f)