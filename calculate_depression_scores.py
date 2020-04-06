import os

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


# 使用 TF-IDF 算法赋予每个词语不同的权值
def get_weights(word_total_count_dict, word_file_count_dict):
    weights = dict()
    return weights


# calculate depression scores for each subject
def calculate_depression_score(weights, words_count):
    return 0


depression_scores = calculate_depression_scores()
print(depression_scores)
