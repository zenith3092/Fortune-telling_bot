#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for love

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_love = True
userDefinedDICT = {"下屬": ["員工", "下屬", "職員"], "健康": ["身體", "健康"], "募資": ["募資"], "學業": ["學業", "課業", "功課", "成績", "考試", "考運"], "工作": ["工作", "職務", "職位", "求職"], "愛情": ["愛情", "桃花", "感情"], "老闆": ["老闆", "上司", "主管"], "考試": ["期中考", "期末考", "月考", "模擬考", "考試", "檢定考", "上機考"], "運勢": ["運勢"], "另一半": ["另一半", "男友", "女友", "老公", "老婆", "太太", "先生"], "研究所": ["研究所"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_love:
        print("[love] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我][單身]很久，不知道[自己][下]個桃花何時[才][會]出現":
        # write your code here
        pass

    if utterance == "[我][會]有姻緣嗎":
        # write your code here
        pass

    if utterance == "[我]何時[可以]脫離母胎[單身]":
        # write your code here
        pass

    if utterance == "[我]想問[我]跟另一半兩人相處狀況":
        # write your code here
        pass

    if utterance == "[我]想算愛情":
        # write your code here
        pass

    if utterance == "[我]的愛情運何時[才][可以][順利][點]":
        # write your code here
        pass

    if utterance == "想要請問[我]的正緣何時[才][會]出現":
        # write your code here
        pass

    return resultDICT