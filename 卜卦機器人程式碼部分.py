#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random
import numpy as np
import pandas as pd
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
