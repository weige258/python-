list_a=[1,2,3]
num=0
def digui(input_list:list):
    global num
    if len(input_list)==0:
        print("完成一次排列组合")
        num+=1
    else:
        for i in range(0,len(input_list)):
            new_list=input_list[:i]+input_list[i+1:]
            digui(new_list)
digui(list_a)
print("总共有排列组合",num)