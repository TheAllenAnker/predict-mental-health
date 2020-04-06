import re
import jieba
import pyexcel
import os

# 使用Jieba依次对每个用户的微博文本文件进行处理，并生成一个仅存有分词结果的文件
raw_file_list = os.listdir('user_raw_contents')
print(raw_file_list)
count = 1
for raw_file_name in raw_file_list:
    word_total_count = dict()
    word_file_count = dict()
    sheet = pyexcel.get_sheet(file_name='user_raw_contents/' + raw_file_name)
    # 处理该用户的每条微博
    for row in sheet:
        # 读取一条微博的初始内容
        # 数据清洗
        post_raw_content = re.sub('(#(.*?)#)|(@(.*?)，)|(@(.*).?)', '', row[1])
        # 数据分词
        post_seg_list = jieba.cut(post_raw_content)
        word_set = set()
        for seg in post_seg_list:
            if seg in word_total_count:
                word_total_count[seg] += 1
            else:
                word_total_count[seg] = 1
                word_file_count[seg] = 0

            if seg not in word_set:
                word_set.add(seg)
                word_file_count[seg] += 1

    # 将字典转化为数组
    word_total_count_arr = []
    word_file_count_arr = []
    for key, val in word_total_count.items():
        word_total_count_arr.append([key, val])
    for key, val in word_file_count.items():
        word_file_count_arr.append([key, val])

    print(word_total_count_arr)
    print(word_file_count_arr)
    saved_word_total_sheet = pyexcel.Sheet(word_total_count_arr)
    saved_word_file_count_sheet = pyexcel.Sheet(word_file_count_arr)
    saved_word_total_sheet.save_as('jieba_processed_contents/word_total/' + str(count) + '_word_total.csv')
    saved_word_file_count_sheet.save_as(
        'jieba_processed_contents/file_total/' + str(count) + '_total_file_count.csv')
    count += 1
