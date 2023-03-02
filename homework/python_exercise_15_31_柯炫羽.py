#導入模組
import pandas as pd
import numpy as np

#讀取資料，並轉成ndarray
df=pd.read_csv('read.csv')
df=np.array(df)

print('資料型態 : ',type(df))
print('平均值 : %.2f'% np.mean(df))
print('中位數 : %.2f'% np.median(df))
print('標準差 : %.2f'% np.std(df))
print('變異數 : %.2f'% np.var(df))
print('極差值 : %.2f'% np.ptp(df))