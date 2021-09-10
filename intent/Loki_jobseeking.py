#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for jobseeking

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_jobseeking = True
userDefinedDICT = {"事業": ["事業", "工作", "工程", "案子", "標案", "事業運", "募資", "計畫", "企劃", "企劃案", "事業狀況"], "單身": ["單身", "母胎單身"], "學業": ["學業", "功課", "考試", "升學", "升高中", "升大學", "高中", "大學", "學測", "研究所", "期中考", "期末考", "月考", "模擬考", "檢定考", "檢定", "上機考", "學業運", "考運", "考試運", "考試情形", "考試狀況"], "愛情": ["愛情", "感情", "婚姻", "姻緣", "正緣", "桃花", "桃花運", "愛情運", "感情運", "感情狀況"], "求職": ["求職運", "找工作", "面試", "求職狀況", "求職情況"], "考試": ["學測", "會考", "期中考", "期末考", "月考", "模擬考", "檢定考", "檢定", "上機考"], "脫單": ["脫單"], "運勢": ["運勢", "流年", "運氣", "手氣"], "另一半": ["另一半", "男友", "女友", "老公", "老婆", "太太", "先生"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_jobseeking:
        print("[jobseeking] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我][之後]有[一場]面試":
        resultDICT["ask"]="求職"

    if utterance == "[我]想[找工作]":
        if args[1] in userDefinedDICT["求職"]:
            resultDICT["ask"]="求職"

    if utterance == "[我]想問[求職]":
        if args[1] in userDefinedDICT["求職"]:
            resultDICT["ask"]="求職"

    if utterance == "[我]想問[求職][順]不[順利]":
        if args[1] in userDefinedDICT["求職"]:
            resultDICT["ask"]="求職"

    if utterance == "[我]想算[求職]":
        if args[1] in userDefinedDICT["求職"]:
            resultDICT["ask"]="求職"

    if utterance == "[我]想算[求職][順]不[順利]":
        if args[1] in userDefinedDICT["求職"]:
            resultDICT["ask"]="求職"

    if utterance == "[我]想算關於[求職]的部分":
        if args[1] in userDefinedDICT["求職"]:
            resultDICT["ask"]="求職"

    if utterance == "[我]想請問[最近]的[求職狀況]如何":
        if args[2] in userDefinedDICT["求職"]:
            resultDICT["ask"]="求職"

    if utterance == "[我]想請問[求職]":
        if args[1] in userDefinedDICT["求職"]:
            resultDICT["ask"]="求職"

    if utterance == "[我]有[個]面試":
        resultDICT["ask"]=""

    if utterance == "不知道結果如何":
        # write your code here
        pass

    if utterance == "[我][想][問][最近]的[求職狀況]":
        # write your code here
        pass

    if utterance == "[我][想][問][求職]":
        # write your code here
        pass

    if utterance == "[我][想][問][求職][順]不[順利]":
        # write your code here
        pass

    if utterance == "[我][想][算]關於[求職]的部分":
        # write your code here
        pass

    if utterance == "[我][想][請問][最近]的[求職狀況]如何":
        # write your code here
        pass

    if utterance == "[最近][找工作][屢屢]撲空":
        # write your code here
        pass

    if utterance == "[最近][求職]不太好":
        # write your code here
        pass

    if utterance == "[最近]的[求職運]不是很好":
        # write your code here
        pass

    return resultDICT