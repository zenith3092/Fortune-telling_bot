#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for career

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_career = True
userDefinedDICT = {"下屬": ["員工", "下屬", "職員"], "健康": ["身體", "健康"], "募資": ["募資"], "學業": ["學業", "課業", "功課", "成績", "考試", "考運"], "工作": ["工作", "職務", "職位", "求職"], "愛情": ["愛情", "桃花", "感情"], "老闆": ["老闆", "上司", "主管"], "考試": ["期中考", "期末考", "月考", "模擬考", "考試", "檢定考", "上機考"], "運勢": ["運勢"], "另一半": ["另一半", "男友", "女友", "老公", "老婆", "太太", "先生"], "研究所": ["研究所"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_career:
        print("[career] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我][最近]公司發展":
        # write your code here
        pass

    if utterance == "[我][最近]接了[一個]專案，不知道發展如何":
        # write your code here
        pass

    if utterance == "[我][最近]有[個]投資案，不知道能否得標":
        # write your code here
        pass

    if utterance == "[我]想算工作":
        # write your code here
        pass

    if utterance == "上司跟下屬關係":
        # write your code here
        pass

    if utterance == "事業發展":
        # write your code here
        pass

    if utterance == "想要募資，不知道能否[順利]":
        # write your code here
        pass

    if utterance == "經營發展順不[順]":
        # write your code here
        pass

    return resultDICT