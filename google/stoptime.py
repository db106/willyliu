"""
資料來源: stop.txt
執行結果: 將停留時間轉為可抓取的值
2.本程式會儲存1個檔案： stoptime.json
"""

import json

path_dir = 'E:\專題\google'
stoptime_js = {}
with open(r'E:\專題\google\writeto\stop_0511.txt', 'r', encoding="utf-8") as p:
    for i in p.readlines():  # 逐筆讀取
        each_content = json.loads(i)  # 將各筆轉成json
        # print(type(each_content), each_content)
        place_word = each_content.get('地點') # ; print(place_word)
        stoptime_word = each_content.get('停留時間') # ; print(stoptime_word)

        if stoptime_word.find('到') > 0: # 訪客通常會在此停留 20 分鐘到 1 小時
            seperate_1 = stoptime_word.split('到')[0]
            s_1 = ''.join(([x for x in seperate_1 if x.isdigit()]))
            seperate_2 = stoptime_word.split('到')[1]
            s_2 = ''.join(([x for x in seperate_2 if x.isdigit()]))

            if s_1 > s_2:
                # stay_s1s2 = (int(s_1)/60 + int(s_2))/2
                staytime = (int(s_1) / 60 + int(s_2)) / 2
                # print('停留時間:', staytime, '小時')

        elif stoptime_word.find('-') > 0: # 訪客通常會在此停留 1-2 小時
            seperate_3 = stoptime_word.split('-')[0]
            s_3 = ''.join(([x for x in seperate_3 if x.isdigit()]))
            seperate_4 = stoptime_word.split('-')[1]
            s_4 = ''.join(([x for x in seperate_4 if x.isdigit()]))
            # stay_s3s4 = (int(s_3) + int(s_4)) / 2
            staytime = (int(s_3) + int(s_4)) / 2
            # print('停留時間:', staytime, '小時')

        elif stoptime_word.find('.') > 0:
            seperate_5 = stoptime_word.split('過')[1]
            # s_5 = float(seperate_5.split(' 小時')[0])
            staytime = float(seperate_5.split(' 小時')[0])
            # print('停留時間:', staytime, '小時')

        else:
            staytime = ''.join(([x for x in stoptime_word if x.isdigit()]))
            # print('停留時間:', staytime, '小時')

        stoptime_js[place_word] = staytime
        print(place_word, ': 停留時間', staytime, '小時')

# 存檔
    print(stoptime_js)
    with open(r'E:\專題\google\writeto' + '\\' + 'stoptime' + '.json', 'a', encoding='utf8') as f:
        save_stoptime = json.dumps(stoptime_js, ensure_ascii=False)
        f.write(save_stoptime)
