'''
郑映慧 1619100019   2019/04/08
function：
    读取指定文件aapl.csv，求算'Volume'列的平均值并输出
'''

import pandas

df = pandas.read_csv(r'E:\University\study\2018-2019\python\homework\6\aapl.csv')
df = df[['Volume']]
ave = df.sum()/df.__len__()
print("平均值：\n",ave)