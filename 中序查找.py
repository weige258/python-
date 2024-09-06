
list_to_search=[1,2,3,6,7,9,12]
search=9

start_index=0
end_index=len(list_to_search)
while start_index<end_index:
    middle_index=int((start_index+end_index)/2)
    print("和查找数据对比的中序索引是",middle_index,"索引的数据是",list_to_search[middle_index])
    if search>list_to_search[middle_index]:
        start_index+=1
    if search<list_to_search[middle_index]:
        end_index-=1
    if list_to_search[middle_index]==search:
        print("找到search1在索引",middle_index,"数据是",list_to_search[middle_index])
        break