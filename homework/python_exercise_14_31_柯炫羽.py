#匯入模組
import matplotlib.pyplot as plt
import numpy as np

#設定資料
data1=[1,4,9,16,25,36,49,64]
data2=[1,2,3,6,9,15,24,39]

#設定圖表
#設定畫布
plt.Figure(facecolor='lightgreen')
#設定圖表標題
plt.title('Figure',fontsize=24)
#設定X、Y軸標題
plt.xlabel('x-Value',fontsize=16)
plt.ylabel('y-Value',fontsize=16)
#設定軸座標刻度
plt.xlim(0,8)
plt.ylim(0,70)
#將資料帶入圖表
plt.plot(np.arange(1,9),data1,'b.--',np.arange(1,9),data2,'r.--',linewidth=1)

#顯示圖表
plt.show()
