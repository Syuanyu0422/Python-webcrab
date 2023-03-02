import pandas as pd
score=[[75,62,85,73,60],[91,53,56,63,65],[71,88,51,69,87],[69,53,87,74,70]]

df=pd.DataFrame(score,\
                index=['小林','小黃','小陳','小美'],\
                    columns=['國文','數學','英文','自然','社會'])
print(df)
print()
print('後兩位的成績')
print(df.tail(2))
print()
print('以自然遞減排序')
print(df.sort_values('自然',ascending=False).loc[:,'自然'])
print()
print('第一、三位學生的數學與自然成績')
print(df.iloc[[0,2],[1,3]])

