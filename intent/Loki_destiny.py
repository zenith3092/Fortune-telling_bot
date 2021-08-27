#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for destiny

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_destiny = True
userDefinedDICT = {"下屬": ["員工", "下屬", "職員"], "健康": ["身體", "健康"], "募資": ["募資"], "學業": ["學業", "課業", "功課", "成績", "考試", "考運"], "工作": ["工作", "職務", "職位", "求職"], "愛情": ["愛情", "桃花", "感情"], "老闆": ["老闆", "上司", "主管"], "考試": ["期中考", "期末考", "月考", "模擬考", "考試", "檢定考", "上機考"], "運勢": ["運勢"], "另一半": ["另一半", "男友", "女友", "老公", "老婆", "太太", "先生"], "研究所": ["研究所"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_destiny:
        print("[destiny] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我]想算運勢":
        # write your code here
        pass

    if utterance == "[我]想請問[最近]的運勢":
        # write your code here
        pass

    if utterance == "[我]想請問[最近]的運勢如何":
        # write your code here
        pass

    return resultDICT