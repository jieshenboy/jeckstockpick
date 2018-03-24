#-*- coding:utf-8 -*-
# 3. 定义函数，实现生成 n 个 点坐标(x , y), 每生成10个点后，
# 调用回调函数 并将生成 10个点 和 开始生成10个点的时间戳，			在回调函数中 将 10个点和时间信息写入到 pots.dat文件中。
# 要求： 时间要转成yyyy-mm-dd hh:mm:ss 格式，
# 每一次信息都在同一行
# 文件模式： ‘a+b’
import random
import time
import datetime
def make_port():
    x = random.randint(0,9)
    y = random.randint(0,9)
    return (x,y)
def n_port(n,make_port):
    fileObject = open('point_time.txt', 'w')
    for j in range(0,n):

        for i in range(0, n):
            fileObject.write(make_port())
        fileObject.write('\n')
        now_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        fileObject.write(now_time)
        fileObject.write('\n')



'''   
def add_time(n,n_port):
    for i in range(0,n):


def port_time(make_port, n):
    for i in range(0,n):
        fileObject = open('point_time.txt', 'w')
        now_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        port_xy = str(make_port())
        print(port_xy+'+'+now_time)
'''
if __name__ == "__main__" :
    n_port(10, make_port)

'''
l = []
def sarpper(fn,start,end,x):
    for j in range(x):
        start = time.time()
        ss = time.localtime(start)
        sss = time.strftime("%Y-%m-%d %H:%M:%S", ss)
        for i in range(10):
            if i % 10 == 0:
                x = random.uniform(start, end)
                y = random.uniform(start, end)
                p = (x, y)
                l.append(p)

    fn(l,sss)


def ab(path):
    with open("pots.dat", "a+b") as f:
        f_content = f.read()
        f.write(bytes(l + "\n", encoding="utf-8")

sarpper(15,20,50)
'''