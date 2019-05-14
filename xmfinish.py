import os
import pickle
os.chdir('D:/python/xm/')
f = open('商铺数据.csv','r',encoding = 'UTF-8-sig')

# 读取第一行
shouHang=f.readline().strip()
shouHang=shouHang.split(',')
# print(shouHang)
# f.seek(0) 第一条无效，不用指针还原
#继续读取其余数据并存储到m
m=[]
n=0
for line in f.readlines():
    n+=1
    st1 = line.strip()
    st1 = st1.split(',')
    am = []
    for i in range(0,len(shouHang)):
       am.append([shouHang[i],st1[i]]) 
    m.append(dict(am))
f.close() # 关闭文件
# m.pop(0) #无需删除第一条数据
print(m[0])
print('ALL DATA IS %i'%n)
print('数据条数：',len(m))
# 清洗函数定义
def rjCh(s1): #人均清洗
    ns2 = s1.split('￥')
    if len(ns2)>= 2 and ns2[1].isdigit():
        nob = int(ns2[1])
    else:
        nob = None
    return nob   
def dpCh(s2): #点评清洗
    ns2 = s2.split(' ')
    if ns2[0].isdigit():
        nob = int(ns2[0])
    else:
        nob = None
    return nob
def pjCh(pj): #评价清洗
    ns = pj.split('                                ')
    if len(ns) == 3 :
        for i in range(3):
            ns[i] = float(ns[i][2:])
        return ns
    else:
        return None
#开始清洗
print('开始清洗点评和人均')
for sj in m:
    sj['comment'] = dpCh(sj['comment'])
    sj['price'] = rjCh(sj['price'])
    sj['commentlist'] = pjCh(sj['commentlist'])
print('清洗点评、评价，人均完毕')
# for i in range(10,15):
    # print(m[i]['price'],m[i]['comment'],m[i]['commentlist'])
print('开始清理无效数据')
for sj in m:
    if sj['comment'] == None or sj['price'] == None :
        m.remove(sj)
print('清理结束，剩余数据条数：',len(m))
#数据存为pkl文件
print('开始存储为pkl文件')
savePkl = open('D:/python/xm/xmData.pkl','wb')
pickle.dump(m,savePkl)
savePkl.close
print('已经存储为pkl文件')


    
