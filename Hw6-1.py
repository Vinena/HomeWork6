'''
郑映慧 1619100019   2019/04/08
function：
    1、随机产生50个数字，存一个列表（list）中；
    2、将list中的数据从小到大排序，然后写入文件sort.txt的第一行中;
    3、从文件中读取文件内容，然后反序，再追加到文件的下一行中。
'''

import random

#生成随机列表、复制列表并从小到大排序
list = [random.randint(1,100) for i in range (50)]
line_one = list 
line_one.sort()

#生成/清空文件
f0=open('E:\sort.txt','w')
f0.write('')
f0.close()

#写入第一行数据
f1=open('E:\sort.txt','a+')
for i in range (len(line_one)):
    f1.write(str(line_one[i]))
    f1.write(',')
f1.close()

#读取第一行数据并逆序
f2=open('E:\sort.txt','r+')
list_two = f2.readline()
f2.close()
line_two = list_two.split(',')

del(line_two[-1])
line_two.reverse()

#写入第二行数据
f3 = open('E:\sort.txt','a+')
f3.write('\n')
for i in range (len(line_two)):
    f3.write(line_two[i])
    f3.write(',')
f3.close()