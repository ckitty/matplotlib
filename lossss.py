import numpy as np
import matplotlib.pyplot as plt
filename1='/home/lichao/陈/终端存储的输出1'
filename2='/home/lichao/陈/终端存储的输出2'
loss=[]
with open(filename1, 'r') as file_to_read:
  while True:
    lines = file_to_read.readline() # 整行读取数据
    if lines.startswith('loss:'):
       s=lines.split(':')
       s=s[1].split('(')
       loss.append(float(s[0]+""))

    if not lines:
        break
with open(filename2, 'r') as file_to_read:
  while True:
    lines = file_to_read.readline() # 整行读取数据
    if lines.startswith('loss:'):
       s=lines.split(':')
       s=s[1].split('(')
       loss.append(float(s[0]+""))

    if not lines:
        break

num=np.array(loss).shape[0]
losss=[]
for i in range(num):
    if (i+1)%4==0:
        losss.append(loss[i])

num2=np.array(losss).shape[0]
loss1=[]
step=50
for j in range(num2):
    if j%50==0:
        loss1.append(losss[j])



num3=np.array(loss1).shape[0]
round=[]
for i in range(num3):
    round.append(i)
plt.plot(round,loss1,label='loss')
plt.xlabel('round*50')
plt.ylabel('loss')
plt.title('Loss-Graph')
plt.legend()
plt.show()




