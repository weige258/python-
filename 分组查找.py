list_to_find=[0,3,4,5,7,8,9,12,14,16,17,19]
search_num=14

#普通for循环查找
common_find_num=0
for i in range(0,len(list_to_find)):
    common_find_num+=1
    if search_num==list_to_find[i]:
        break
print("普通查找要找",common_find_num,"次")

#分组查找
#分组数据5个一组
num_to_group=5
index=0
data_group={}
for i in range(0, int(len(list_to_find)/num_to_group)+1):
    data_group[i]=list_to_find[index:index+num_to_group]
    print(data_group)
    index+=num_to_group
print(num_to_group,"分一组后的数据是",data_group)
#判断要查找的数据是否在一组数据中间
group_by_find_num=0
for i in range(0,len(data_group)):
    group_by_find_num+=1
    print("这组数据是",data_group[i])
    if data_group[i][0]<=search_num<=data_group[i][-1]:
        print("在这组数据中间")
        for x in range(0,len(data_group[i])):
            group_by_find_num += 1
            if search_num==data_group[i][x]:
                print("找到了数字",search_num,"在索引",i*num_to_group+x)
                break
        break
print("分组查找次数",group_by_find_num)