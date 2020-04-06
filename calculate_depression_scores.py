import os
import pyexcel
import math

# 将 NTUSD 的正面、负面情感字典加载入内存
negative_words_file = open('NTUSD_negative_simplified.txt', 'r')
positive_words_file = open('NTUSD_positive_simplified.txt', 'r')
negative_lines = negative_words_file.readlines()
positive_lines = positive_words_file.readlines()
negative_words = set()
positive_words = set()
for line in negative_lines:
    negative_words.add(line.rstrip())
for line in positive_lines:
    positive_words.add(line.rstrip())
print('Negative words in NTUSD: ', negative_words)
print('Positive words in NTUSD: ', positive_words)

# N 为每个用户共收集到的微博条数
N = 100


# 使用 TF-IDF 算法赋予每个词语不同的权值
def get_weights(word_count, file_count):
    weights = dict()
    # 依次计算各个词语的 TF 值，IDF 值，权值（weight）
    for word, word_num in word_count.items():
        if word in file_count:
            tf = word_num / word_total_count
            idf = math.log(N / file_count[word])
            weights[word] = tf * idf
    return weights


# 根据每个用户的词语权值计算每个用户的抑郁分数，抑郁分数的值越大，预测抑郁水平越高
def calculate_depression_score(weights, words_count):
    depression_score, hit_count = 0, 0
    for word, weight in weights.items():
        if word in negative_words:
            depression_score += (words_count[word] * weight)
            hit_count += words_count[word]
        elif word in positive_words:
            depression_score -= (words_count[word] * weight)
            hit_count += words_count[word]
    return depression_score, hit_count


# 计算抑郁分数并将分数按行存入文件中

# 加载词语统计数据
processed_file_list = os.listdir('jieba_processed_contents/word_total')
count = 1
depression_scores = []
word_hit_count = []
for processed_filename in processed_file_list:
    file_num = processed_filename.split('_')[0]
    file_total_filename = str(file_num) + '_total_file_count.csv'
    word_total_filename = str(file_num) + '_word_total.csv'
    word_count_sheet = pyexcel.get_sheet(file_name='jieba_processed_contents/word_total/' + word_total_filename)
    file_count_sheet = pyexcel.get_sheet(file_name='jieba_processed_contents/file_total/' + file_total_filename)
    word_count_dict = dict()
    file_count_dict = dict()
    word_total_count = 0

    # 将两个统计文件中的两列分别存入字典中
    for row in word_count_sheet:
        word_count_dict[row[0]] = int(row[1])
        word_total_count += int(row[1])
    for row in file_count_sheet:
        file_count_dict[row[0]] = int(row[1])

    curr_weights = get_weights(word_count_dict, file_count_dict)
    depression_score, hit_count = calculate_depression_score(curr_weights, word_count_dict)
    depression_scores.append([count, depression_score])
    word_hit_count.append([count, hit_count])
    count += 1

print(depression_scores)
print(word_hit_count)
depression_scores_sheet = pyexcel.Sheet(depression_scores)
depression_scores_sheet.save_as('depression_scores.csv')
word_hit_sheet = pyexcel.Sheet(word_hit_count)
word_hit_sheet.save_as('word_hit_count.csv')
