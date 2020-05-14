
"""
a = ['中央大學', '花開了休閒農場', '八德埤塘生態公園', '新竹市眷村博物館', '新竹市立動物園']
with open(r'E:\專題\google\temp.txt', 'r', encoding="utf-8") as temp:
    all_suggest = temp.read()[2:-2]  # ; print('all_suggest:', all_suggest)
    all_suggest_list = list(all_suggest.split(")("));

for i, article in enumerate(all_suggest_list):
    # print(i)
    if str(a) in article:
        print(i)
        print(article)
"""
# =======
a = ['中央大學', '花開了休閒農場', '八德埤塘生態公園', '新竹市眷村博物館', '新竹市立動物園']
b = [3, ['中央大學', '花開了休閒農場', '八德埤塘生態公園', '新竹市立動物園', '新竹市眷村博物館'], '新竹市眷村博物館', '新竹市立動物園', 7, '3.0',
     4, ['中央大學', '花開了休閒農場', '八德埤塘生態公園', '新竹市眷村博物館', '新竹市立動物園'], '中央大學', '花開了休閒農場', 37, '27.7']

for index, value in enumerate(b):
    if a in b:
        print(index, value)

        with open(r'E:\專題\google\practice' + '\\' + 'test' + '.txt', 'a', encoding='utf8') as f:
            f.write(str(value))
            f.write('\n')
