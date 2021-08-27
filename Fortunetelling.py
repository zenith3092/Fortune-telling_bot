#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 2.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No Match Intent!"
                }
            ]
        }
"""

from requests import post
from requests import codes
import math
import json
import random
import numpy as np
import pandas as pd
try:
    from intent import Loki_love
    from intent import Loki_jobseeking
    from intent import Loki_career
    from intent import Loki_destiny
    from intent import Loki_study
except:
    from .intent import Loki_love
    from .intent import Loki_jobseeking
    from .intent import Loki_career
    from .intent import Loki_destiny
    from .intent import Loki_study

    with open("account.txt", encoding="utf-8") as f:
        accountDICT = json.loads(f.read())
    
    LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
    USERNAME = accountDICT["username"]
    LOKI_KEY = accountDICT["loki_project_key"]
# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "Connect failed."
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST, filterLIST=[]):
    resultDICT = {}
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # love
                if lokiRst.getIntent(index, resultIndex) == "love":
                    resultDICT = Loki_love.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # jobseeking
                if lokiRst.getIntent(index, resultIndex) == "jobseeking":
                    resultDICT = Loki_jobseeking.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # career
                if lokiRst.getIntent(index, resultIndex) == "career":
                    resultDICT = Loki_career.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # destiny
                if lokiRst.getIntent(index, resultIndex) == "destiny":
                    resultDICT = Loki_destiny.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # study
                if lokiRst.getIntent(index, resultIndex) == "study":
                    resultDICT = Loki_study.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)


if __name__ == "__main__":
    ## love
    #print("[TEST] love")
    #inputLIST = ['我想算愛情','我會有姻緣嗎','我何時可以脫離母胎單身','我的愛情運何時才可以順利點','想要請問我的正緣何時才會出現','我想問我跟另一半兩人相處狀況','我單身很久，不知道自己下個桃花何時才會出現']
    #testLoki(inputLIST, ['love'])
    #print("")

    ## jobseeking
    #print("[TEST] jobseeking")
    #inputLIST = ['接下來要找工作，不知道是否順利','下周有個工作面試，想要問面試結果好嗎']
    #testLoki(inputLIST, ['jobseeking'])
    #print("")

    ## career
    #print("[TEST] career")
    #inputLIST = ['事業發展','我想算工作','上司跟下屬關係','我最近公司發展','經營發展順不順','想要募資，不知道能否順利','我最近有個投資案，不知道能否得標','我最近接了一個專案，不知道發展如何']
    #testLoki(inputLIST, ['career'])
    #print("")

    ## destiny
    #print("[TEST] destiny")
    #inputLIST = ['我想算運勢','我想請問最近的運勢','我想請問最近的運勢如何']
    #testLoki(inputLIST, ['destiny'])
    #print("")

    ## study
    #print("[TEST] study")
    #inputLIST = ['我想算學業','我期中考結果如何','我今年要考公職考試，會考上嗎','想要請問我明年的研究所考試結果']
    #testLoki(inputLIST, ['study'])
    #print("")

    # 輸入其它句子試看看
    inputLIST = ["輸入你的內容1", "輸入你的內容2"]
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Result => {}".format(resultDICT))
    
    #利用Loki判斷ask
    ask="愛情"
    #開頭引導句
    #互動第一句
    num1=random.randint(1,2)
    num2=random.randint(1,2)
    num3=random.randint(1,2)
    #互動第二句
    num4=random.randint(1,2)
    num5=random.randint(1,2)
    num6=random.randint(1,2)
    #結果呈現
    gua=int(str(num6)+str(num5)+str(num4)+str(num3)+str(num2)+str(num1))
    data = pd.read_csv('卜卦機器人資料庫.csv',encoding='utf-8')
    for i in range(0,64):
        if gua == data.iloc[i,0]:
            print("您占卜到的卦象為：",data.iloc[i,2],"\n在此給予您小建議：")
            print(data.iloc[i,4])
            print("\n另外，根據您占卜之面向為：",ask)
            print("占卜的結果顯示：\n"," ",data.iloc[i][ask])    