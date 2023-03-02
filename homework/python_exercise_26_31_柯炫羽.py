import requests
import json
import math
from collections import Counter

OMDB_URL = 'http://www.omdbapi.com/?apikey=d214c532'


def get_data(url):
    #data = json.loads(requests.get(url).text)   
    data = requests.get(url).json()
    if data['Response'] == 'True':
        return data
    else:
        return None

def search_ids_by_keyword(keywords):
    movie_ids = list()
    query = '+'.join(keyword.split())  # e.g., "Iron Man" -> Iron+Man

    url = OMDB_URL + '&s=' + query
    data = get_data(url)

    if data:
        # 取得第一頁電影 id
        for item in data['Search']:
            movie_ids.append(item['imdbID'])
        # 取得搜尋結果總數
        total = int(data['totalResults'])
        num_pages = math.ceil(total/10) 

        # 取得第二頁以後的資料
        for i in range(2, num_pages+1):
            url = OMDB_URL + '&s=' + query + '&page=' + str(i)
            data = get_data(url)
            if data:
                for item in data['Search']:
                    movie_ids.append(item['imdbID'])
    return movie_ids

def search_by_id(movie_id):
    url = OMDB_URL + '&i=' + movie_id
    data = get_data(url)
    return data if data else None 

keyword =  'iron man'
m_ids = search_ids_by_keyword(keyword)
# print('關鍵字 %s 共有 %d 部影片' % (keyword, len(m_ids)))
# print('取得影片資料中...')
movies = list()
for m_id in m_ids:
    movies.append(search_by_id(m_id))
print('影片資料範例 first20:')
for m in movies[:20]:
    print('Title:',m['Title'],'Year:',m['Year'],'imdbID:',m['imdbID'])

types = [m['Type'] for m in movies]
# collections.Counter() 會統計一個 list 中各項目出現的次數, 並回傳一個 dict
types_count = Counter(types)
print('電影種類及數量:', types_count)

    
    
