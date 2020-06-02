import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import os
import urllib.request

# 讀取檔案
# classes = 'AWS', 'BI', 'Block_Chain', 'DM', 'Docker', 'IOT', 'IOT2-KAFKA', 'Line-Chatbot', 'Linux', 'NoSQL', 'PyAI',\
#           'PyETL', 'Python', 'R', 'Spark'

classes = 'AWS', 'BI'
for suject in classes:
    classes_filename = suject + '.txt'

    os.chdir(r'/Users/willy/Documents/TibaMe/tibame_class/urls')
    f = open(classes_filename).readlines()

    for n in range(0,len(f)):
        file_info = (f[n].split('\n'))
        if file_info[0] == '':
            pass

        else:
            filename = file_info[0].split(' : ')[0]
            # filename = suject + ' ' + filename.replace('/', '_')
            filename = suject + ' ' + filename.replace('/', '_') + '.mp4'
            url = file_info[0].split(' : ')[1]
            # print(filename, url)


# 存影像檔
        os.chdir(r'/Users/willy/Documents/TibaMe/tibame_class')
        save_path = '/Users/willy/Documents/TibaMe/tibame_class/' + suject

        if not os.path.exists(suject):
            os.mkdir(save_path)

        else:
            os.chdir(save_path)
            urllib.request.urlretrieve(url, filename)
            print('已存檔:', filename, url)
            print()

