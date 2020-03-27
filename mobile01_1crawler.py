import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from urllib import request
from bs4 import BeautifulSoup
import os
import time
import requests
import json

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

# 列表 =====
area = {188:'基隆市', 189:'台北市', 190:'新北市', 191:'桃園市', 192:'新竹市', 193:'新竹縣', 209:'宜蘭縣'}
print(area.items())
# num = input('請輸入縣市代碼: ')

for num in (188, 189, 190, 191, 192, 193, 209):
# for num in (190, 192):

# 建立資料夾 =====
    path_dir = 'E:\專題\\Mobile01\\json' # E:\專題\Mobile01\json

# 爬取列表 =====
    print('開始爬取:', area.get(int(num)))

    url_p1 = 'https://www.mobile01.com/topiclist.php?f=' + str(num) # https://www.mobile01.com/topiclist.php?f=188
    req = request.Request(url=url_p1, headers=headers)
    res = request.urlopen(req)
    # print(res.read().decode('utf-8')) # 查看列表原始碼
    content_p1 = BeautifulSoup(res, 'html.parser')
    # print(content_p1)
    title_txt = content_p1.select('div[class="c-listTableTd__title"] a[class="c-link u-ellipsis"]')

# 總頁數 =====
    total_pages = int(content_p1.select('div[class="l-navigation__item l-navigation__item--min"], a[class="c-pagination"]')[-1].text) +1

# 列表頁 =====
    page = 1
    while page < total_pages:
        url = 'https://www.mobile01.com/topiclist.php?f=' + str(num) + '&p={0}'.format(page) # https://www.mobile01.com/topiclist.php?f=188&p=26
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        content_all = BeautifulSoup(res, 'html.parser')
        title_txt = content_all.select('div[class="c-listTableTd__title"] a[class="c-link u-ellipsis"]')
        print('page', page, ':', url)

# 特殊符號 =====
        for n in range(0,30):
            try:
                title_replace = title_txt[n].text
                title_save = title_replace[0:10].replace('*','').replace('|','').replace('\\','').replace(':','')\
                .replace('\"','').replace('<','').replace('>','').replace(']','').replace('[','').replace('?','')\
                .replace('/','').replace('《','').replace('》','').replace('・','').replace('/','').replace('，','')\
                .replace('「','').replace('」','').replace('！','').replace('｜','').replace('【','').replace('】','')\
                .replace('？','').replace('、','').replace('.','').replace('’','').replace('–','').replace('～','')\
                .replace('?','').replace('#','').replace('!','').replace('(','').replace(')','').replace('~','')\
                .replace('、','').replace('『','').replace('』','').replace('，','').replace('-','').replace('\\n','') \
                    .replace('*', '')

            except:
                title_save = "title pass"
                print(title_save)

# 文章序號 =====
            try:
                url_back = title_txt[n]['href'][12:]
                url_article = 'https://www.mobile01.com/topicdetail.' + url_back # 文章網址
                serial = url_article.split('=')[-1] # 文章序號

            except:
                print('article serial pass')

# 判斷文章是否已存在 =====

            if not os.path.exists(path_dir):
                os.mkdir(path_dir)
            os.chdir(path_dir)

            # os.chdir('E:\專題\\Mobile01\\json')
            serial_txt = 'Mobie01_serial.txt'
            f = open(serial_txt, mode='a', encoding='utf8' + '\n')
            content_txt = open(serial_txt)
            serial_content = content_txt.read()
            serial = url_back.split('=')[-1]

            if serial in serial_content:
                print(area.get(int(num)), 'page', page, 'of', total_pages-1, ':文章編號' + serial + ' 已存在')

            else:
                f = open(serial_txt, mode='a', encoding='utf8' + '\n')
                f.write(serial + '\n')

# 標題及建立文章資料夾 =====
                try:
                    title_0 = (title_txt[n].text) # 完整標題
                    # title = ('"標題":"' + title_save + '",')
                    # path_dir_each = path_dir + '\\' + title_save # 取標題前20字元為資料夾名稱
                    path_dir_each = path_dir + '\\' + title_0  # 取標題前20字元為資料夾名稱

                except:
                    title = "title pass"
                    print(title)

# 網址 =====
                try:
                    url_back = title_txt[n]['href'][12:]
                    url_article = 'https://www.mobile01.com/topicdetail.' + url_back
                    url_article_1 = ('{"文章網址":"' + url_article + '",')

                except:
                    url_article = "https://www.Nodata_url_article"
                    print(url_article)

# 內文 =====
                try:
                    url_back = title_txt[n]['href'][12:]
                    url_article = 'https://www.mobile01.com/topicdetail.' + url_back

                    req_con = request.Request(url=url_article, headers=headers)
                    res_con = request.urlopen(req_con)
                    soup_con = BeautifulSoup(res_con, 'html.parser')
                    # print('soup_con:', soup_con)

                    article = soup_con.select('div[itemprop="articleBody"] ')[0].text.strip()
                    article_1 = ('"文章內容":"' + article + '",')

                    postdate = soup_con.select('span[class="o-fNotes o-fSubMini"]')[0].text
                    postdate_1 = ('"發文日期":"' + postdate + '",')

                except:
                    print('article or postdate pass')

# 存成一個檔(標題+內容)
                try:
                    os.chdir('E:\專題\\Mobile01\\')
                    f = open('Mobile01_all.txt', mode='a', encoding='utf8') # E:\專題\Mobile01\Mobile01_all.txt
                    f.write(title_replace + '\n' + article + '\n')
                    print('already write to all')

                except:
                    print('os.chdir pass')

# 存檔 =====
                if not os.path.exists(path_dir):
                    os.mkdir(path_dir)
                os.chdir(path_dir)
                # f = open(title_save + serial + '.json', mode='a', encoding='utf8')
                f = open(serial + '.json', mode='a', encoding='utf8')
                # f.write(url_article_1)  # 寫入網址

                total = {'文章網址':url_article,
                           '發文時間':postdate,
                           '標題':title_0,
                           '景點名稱':'NA',
                           '文章內容':article,
                           '留言':'NA',
                           '地址':'NA',
                           '縣市':area.get(int(num))
                           }
                total_k = json.dumps(total, ensure_ascii=False)
                f.write(total_k)
                # print('已寫入:', total_k)
                print(area.get(int(num)), 'Page', page, 'of', total_pages-1, ' 存檔完成', '......', '文章編號:' + serial + '、' + '標題:', title_0)

        # time.sleep(random.randint(1, 3))
        page += 1

print('所有文章存檔完成!!! at', time.asctime())

# Line通知
def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
    return r.status_code

message = 'Mobile01的所有文章存檔完成 at ', time.asctime() # 修改為你要傳送的訊息內容


token = os.environ.get("linetk") # 修改為你的權杖內容

lineNotifyMessage(token, message)

"""存檔格式
{
"文章網址": "",
"發文時間": "",
"標題": "",
"景點名稱": "", 
"文章內容": "",  
"留言": ["" ,"",.....],
"地址": "", 
"縣市": "",
}
"""
