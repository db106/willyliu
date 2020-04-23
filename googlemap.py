"""
資料來源: 景點名.txt
執行結果:
1.計算出從Google地圖查詢所有地點之間的距離和交s通時間
2.本程式會儲存1個檔案： use.txt
"""

import os
import time
import json
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from itertools import combinations, permutations

path_dir = 'E:\專題\google'
if not os.path.exists(path_dir):
    os.mkdir(path_dir)

driver = Chrome('./chromedriver')

url = 'https://www.google.com.tw/maps/dir///@24.9554014,121.2384829,17z/data=!4m2!4m1!3e0?hl=zh-TW'

search_tag_list = []

with open(r'E:\專題\google\writeto\景點名.txt', 'r', encoding="utf-8") as f:
    f = f.readlines()
    # print(f)

    for each_line in f:
        if each_line not in search_tag_list:
            search_tag_list.append(each_line)

    # search_tag_list = list(combinations(search_tag_list, 2))
    search_tag_list = list(search_tag_list)
    for start in search_tag_list:
        for end in search_tag_list:
            #print('i:', i)
            if start == end:
                pass
            else:
                # search_tag = i
                #print('search_tag:', search_tag)

                driver.get(url)
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="sb_ifc50"]/input').send_keys(start.replace('\n', ''))  # --- 輸入起點
                # print(start)
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input').send_keys(end.replace('\n', ''))  # --- 輸入目的
                # print(k)
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input').send_keys(Keys.ENTER)
                time.sleep(5)
                driver.find_element_by_css_selector('span#section-directions-trip-details-msg-0').click()
                time.sleep(3)
                # html = driver.page_source
                # print(html)

                soup = BeautifulSoup(driver.page_source, 'html.parser')
                # print(soup)

                a = soup.select('h1[class="section-trip-summary-title"]')
                c = soup.select('h2[class="directions-mode-group-title"]')
                # print(c)
                address = [d.text for d in c]

                # print(b)
                for i in a:
                    # print(i.text.split('-')[0])
                    time.sleep(1)

                    save_data_dict = {'出發地點': start.replace('\n', ''),
                                      '目的地': end.replace('\n', ''),
                                      '所需時間': i.text.split('-')[0],
                                      '路徑': address}
                    print(save_data_dict)

                    save_data_js = json.dumps(save_data_dict, ensure_ascii=False)

                    with open(r'E:\專題\google\writeto' + '\\' + 'use' + '.txt', 'a', encoding='utf8') as f:
                        f.write(save_data_js)
                        f.write('\n')

driver.close()
