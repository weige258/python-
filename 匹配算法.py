#匹配算法 从一个文本中找输入的词汇或文本
text="我是男生 我是男孩 我是女人 一个男孩子"
search="男孩"

for text_index in range(0,len(text)):
    num=0
    for search_index in range(0,len(search)):
         try:
             if search[search_index]==text[text_index+search_index]:
                 num+=1
             if num==len(search):
                 print(f"找到在索引{text_index}到{text_index+search_index}")
         except:
             continue

