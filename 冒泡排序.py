
list_need_to_sort=[2,6,3,7,8,1]

for loop in range(len(list_need_to_sort)):
    for i in range(0,len(list_need_to_sort)-1):
        if list_need_to_sort[i]>list_need_to_sort[i+1]:
            t=list_need_to_sort[i]
            list_need_to_sort[i]=list_need_to_sort[i+1]
            list_need_to_sort[i+1]=t
            print(f"已经进行一次位置交换{list_need_to_sort}")
print("最终排序结果"+str(list_need_to_sort))