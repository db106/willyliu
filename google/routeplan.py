"""
資料來源: 景點名.txt、use.txt
執行結果:
1.從Google抓各景點的停留時間
2.本程式會儲存2個檔案： routeplan.txt, suggest.txt
"""

from itertools import combinations, permutations
import json
# 列出所有的排列組合
path_dir = 'E:\專題\google'

with open(r'E:\專題\google\writeto\景點名.txt', 'r', encoding="utf-8") as p:
    p = p.read().splitlines() # ; print('p:', p)
    p_start = p[0] # ; print('p_start:', p_start)
    p_go = p[1:] # ; print('p_path:', p_go)
    p_num = len(p)
    perm_all = list(permutations(p, p_num)) # ; print('perm_all:', perm_all) # 所有排列組合



    vs_distance = {}
    for a in range(0,len(perm_all)):
        # print('perm_all[a])[0]', list(perm_all[a])[0])
        # print('p[0]', p[0])
        if list(perm_all[a])[0] == p[0]:
            path = list(perm_all[a])
            print('試算路線',a+1, ':', path)
            # print('check:', list(perm_all[a])[-1])

            all_distance = 0
            all_spend = 0

            # print(path)
            for each in range(0,len(path)-1):
                p_start = path[each]
                p_end = path[each+1]
                # print(each, p_start, each+1, p_end)

# 列出google跑出的資訊
                with open(r'E:\專題\google\writeto\use_0511.txt', 'r', encoding="utf-8") as u:
                    # content_all = u.readlines()

                    for i in u.readlines():  # 逐筆讀取
                        each_content = json.loads(i)  # 將各筆轉成json
                        # print('google txt:', each_content)
                        g_start = each_content.get('出發地點');
                        # print('g_start:', g_start)
                        g_end = each_content.get('目的地');
                        # print('g_end:', g_end)
                        g_spend_time = int(each_content.get('所需時間').split('分 (')[0]);
                        # print('g_spend_time(', g_start, '-', g_end, '):',g_spend_time)
                        g_distance = str(each_content.get('所需時間').split('分 (')[1][:-6]);
                        # print('g_distanc(', g_start, '-', g_end, '):',g_distance)

# 列出所有試算路線
                        if g_start == p_start and g_end == p_end:
                            routeplan = a+1, path, g_start, g_end, g_spend_time, g_distance
                            # print('routeplan:', routeplan)

# 將所有試算路線存檔: routeplan.txt
#                             with open(r'E:\專題\google\writeto' + '\\' + 'routeplan' + '.txt', 'a', encoding='utf8') as f:
#                                 save_stoptime = json.dumps(routeplan, ensure_ascii=False)
#                                 save_stoptime = list(routeplan)
#                                 print(type(save_stoptime), save_stoptime[1])
#                                 f.write(str(routeplan)) # ...存檔
#                                 f.close()

                             # print(g_start, '--', g_end, ': 時間', g_spend_time, '分鐘  距離', g_distance, '公里')
                            all_spend += int(g_spend_time) #; print('all_spend+', all_spend)
                            all_distance += float(g_distance) #; print('all_distance+', all_distance)

# 計算各路線的總時間與總距離
                            if g_end == list(perm_all[a])[-1] or g_start == list(perm_all[a])[-1]:
                                tt_time = all_spend/60 ; print('總時間:', tt_time, '小時')
                                tt_distance = all_distance ; print('總距離:', tt_distance, '公里')
                                vs_distance[str(path)] = all_distance # ; print(type(vs_distance), 'vs_distance:', vs_distance)

                        else:
                            pass
            print()

# 找出最短路徑
    min = min(vs_distance.values())
    min_schadule = list(vs_distance.keys())[list(vs_distance.values()).index(min)]
    print('建議路徑:', '\n', min_schadule, '\n', '總距離:', min, '公里')
    print()

# 存檔
    with open(r'E:\專題\google\writeto' + '\\' + 'suggest' + '.txt', 'a', encoding='utf8') as f:
        place = list(min_schadule[2:-2].split("', '"))
        print('已儲存:', place)
        f.write(min_schadule)
        f.close()
        print()
