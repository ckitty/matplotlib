import numpy as np
import matplotlib.pyplot as plt

filename1='/home/lichao/陈/终端存储的输出1'
filename2='/home/lichao/陈/终端存储的输出2'
data=[]
with open(filename1, 'r') as file_to_read:
  while True:
    lines = file_to_read.readline() # 整行读取数据
    if lines.startswith('[验证阶段]recall_list ='):
        l=[]
        s=lines.split('[')
        s=s[2].split(']')
        s=s[0].split(',')
        for i in range(5):
            l.append(float(s[i]+""))
        data.append(l)

    if not lines:
        break

with open(filename2, 'r') as file_to_read:
  while True:
    lines = file_to_read.readline() # 整行读取数据
    if lines.startswith('[验证阶段]recall_list ='):
        l=[]
        s=lines.split('[')
        s=s[2].split(']')
        s=s[0].split(',')
        for i in range(5):
            l.append(float(s[i]+""))
        data.append(l)

    if not lines:
        break
np_data=np.array(data)
num1=np_data.shape[0]
# 其他 植被 马路 建筑 水体
other=[]
plant=[]
road=[]
archi=[]
water=[]


# 轮数
round=[]


step=50
for j in range(num1):
    if j%step==0:
        other.append(data[j][0])
        plant.append(data[j][1])
        road.append(data[j][2])
        archi.append(data[j][3])
        water.append(data[j][4])

num2 = np.array(other).shape[0]
for x in range(num2):
    round.append(x)
plt.plot(round,other,label='other')
plt.plot(round,plant,label='plant')
plt.plot(round,road,label='road')
plt.plot(round,archi,label='archi')
plt.plot(round,water,label='water')

plt.xlabel('round*50')
plt.ylabel('accuracy')
plt.title('Graph')
plt.legend()
plt.show()



