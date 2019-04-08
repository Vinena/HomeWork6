'''
郑映慧 1619100019   2019/04/08
function：
    按指定的列顺序生成指定的的csv文件
'''

import pandas

list1 = [1,2,3,4,5]
list2 = ['mayi','jack','tom','rain','hanmeimei']
list3 = [18,21,25,19,23]
list4 = [99,89,95,80,81]

df = pandas.DataFrame({'No.':list1,'Name':list2,'Age':list3,'Score':list4})
df=df[['No.','Name','Age','Score']]
df.to_csv(r'E:\Hw6-2.csv',index=False,sep=',')