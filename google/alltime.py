"""
資料來源: suggest.txt、routeplan.txt、stoptime.json
執行結果: 顯示推薦路線的各點交通時間、停留時間，及加總
2.本程式會儲存0個檔案
"""

import json
from decimal import Decimal
import datetime
import math
from datetime import timedelta
import pandas as pd
import numpy as np

path_dir = 'E:\專題\google'

# 載入推薦路線
departure = datetime.datetime(2020, 5, 23, 8, 00, 00)
with open(r'E:\專題\google\writeto\suggest.txt', 'r', encoding="utf-8") as path:
    suggest_path = path.read()[2:-2]
    suggest_path_list = list(suggest_path.split("', '"))
    print('推薦路線:', suggest_path_list)
    print('出發時間:', departure)
    print('出發地點:', suggest_path_list[0])


    for each_path in range(0,len(suggest_path_list)-1):
        # print(suggest_path_list[each_path], '--', suggest_path_list[each_path+1]) # 推薦路線

        sub_tt_time = 0
        departure = departure

# 比對推薦路線在所有推薦的位置
        with open(r'E:\專題\google\writeto\routeplan.txt', 'r', encoding="utf-8") as temp:
            all_suggest = temp.read()[2:-2] # ; print('all_suggest:', all_suggest)
            all_suggest_list = list(all_suggest.split(")(")) # ; print('all_suggest_list:', all_suggest_list)

            for index, content in enumerate(all_suggest_list):
                if str(suggest_path_list) in content:
                    # print(index, content) # 找出推薦的位置及所有內容
                    take = content[len(str(suggest_path_list))+4:].split(",") # ; print('take:', take)
                    trafficetime = round(Decimal((float(take[-2])/60)),1) # 交通時間

    # 載入各點的停留時間
                    with open(r'E:\專題\google\writeto\stoptime.json', 'r', encoding="utf-8") as stop_each:
                        stop_each = json.load(stop_each)
                        stoptime = round(Decimal(stop_each.get(suggest_path_list[each_path + 1])),1) # 停留時間

                        tt_time = trafficetime + stoptime
                        sub_tt_time += tt_time  # 交通+停留時間(累加)

                        if suggest_path_list[each_path] == take[-4][2:-1] and suggest_path_list[each_path+1] == take[-3][2:-1]:
                            stay_min = list(math.modf(tt_time)) # ; print(stay_min)
                            traffic_stay_time = datetime.timedelta(hours=stay_min[1], minutes=stay_min[0] * 60)
                            departure += traffic_stay_time
                            lunch_time_1 = datetime.datetime(2020, 5, 23, 11, 45)
                            lunch_time_2 = datetime.datetime(2020, 5, 23, 13, 30)
                            # print(lunch_time_1)
                            # print(departure)
                            # print(lunch_time_2)
                            if lunch_time_1 < departure < lunch_time_2:
                                print('時間接近用餐時間, 系統搜尋附近餐廳...')
                            # if diff_1 < timedelta(minutes=0) and diff_2 < timedelta(minutes=0):
                            #     print('下個景點的離開時間是', departure, '請先用餐')
                            # else:
                            #     print('a')

# 各欄位數字
                            final = {'出發': take[-4],
                                     '到達': take[-3].split("'")[1],
                                     '距離': take[-1],
                                     '交通時間': trafficetime,
                                     '停留時間': stoptime,
                                     '交通+停留時間': tt_time,
                                     '累積時間': sub_tt_time,
                                     '離開時間': departure
                                     }
                            # print(final)
                            print('開車', final.get('交通時間'), '小時後抵達', final.get('到達'),
                                  '; 預計停留:', final.get('停留時間'), '小時, 離開時間', final.get('離開時間'))


                        else:
                            pass

print('總共時間:', sub_tt_time, '小時', end=', ')
if sub_tt_time > 10:
    print('行程太滿, 請刪減景點!')

elif sub_tt_time < 5:
    print('行程有點少, 請考慮增加景點‧')

else:
    print('總時間適中')
