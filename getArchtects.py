import re
import requests
import pandas as pd


def get_architects_list():
    url = "https://ja.wikipedia.org/w/api.php"

    # ページのタイトルを指定
    params = {
        "action": "parse",
        "page": "日本の建築家一覧",
        "format": "json",
        "prop": "wikitext"
    }

    response = requests.get(url, params=params)
    content = response.json()
    if 'error' in content:
        print("エラーが発生しました:", content['error']['info'])
        return None
    else:
        return content
    


content = get_architects_list()

content_text = content['parse']['wikitext']['*']

matches = re.findall(r'\[\[(.*?)\]\]', content_text)

archList = []
# 抽出された文字列を出力
for match in matches:
    archList.append(match)

#Wikipediaの使用で同姓同名の人がいる場合｜で区切って職業などを表記するためそれを取り除く
archList = [name.split("|")[0] if "|" in name else name for name in archList]

archList = list(dict.fromkeys(archList))


archDf = pd.DataFrame(index=archList, columns=archList)
archDf = archDf.fillna(0)





