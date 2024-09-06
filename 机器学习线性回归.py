#有一群不同年龄的孩子 身高和年龄成线性增长 y=kx+b 求最拟合的k和b
import numpy
#这是身高和年龄的数据
age=   [12,12,14,15,17,18,18]
height=[140,144,160,165,180,175,188]

#初始化三个列表存k b 和总的loss
k_list=[]
b_list=[]
total_loss_list=[]

for k in numpy.arange(0,3,0.1):
    for b in numpy.arange(0,200,1):
        total_loss=0
        for i in range(0,len(age)):
            real_heigth=height[i] #载入每个孩子的真实身高
            real_age=age[i]  #载入每个孩子的年龄
            #计算身高 y=k*年龄+b
            calculated_height=k*real_age+b
            #每个孩子身高的误差是
            loss=abs(real_heigth-calculated_height)
            #添加到总loss
            total_loss+=loss
        k_list.append(k)
        b_list.append(b)
        total_loss_list.append(total_loss)
#求总loss列表里面总loss最小值的索引也就是最拟合的索引
index=total_loss_list.index(min(total_loss_list))
#输出最拟合的k和b值
print("最拟合的k值是",k_list[index],"最拟合的b值是",b_list[index])
print(f"也就是y={k_list[index]} x +{b_list[index]}")

for i in range(0,len(age)):
    real_heigth = height[i]
    real_age = age[i]
    calculated_height=k_list[index]*real_age+b_list[index]
    print("孩子的函数计算身高是",calculated_height,"真实身高是",real_heigth)