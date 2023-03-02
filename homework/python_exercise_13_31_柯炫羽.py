import json
data={'people':[{'id':'1','name':'Peter','country':'Taiwan'},\
                {'id':'2','name':'Jack','country':'USA'},\
                {'id':'3','name':'Cindy','country':'Japan'}]}


with open('write.json','w') as file:    
     json.dump(data,file)
