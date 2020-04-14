from gensim.models import word2vec


def expand_sentiment_dict(potential_words_filename, positive_words_filename, negative_words_filename,
                          total_words_filename):
    # 以所有词语为训练语料训练 Word2vec 模型
    sentences = word2vec.Text8Corpus(total_words_filename)
    word2vec_model = word2vec.Word2Vec(sentences, size=24, min_count=1)
    # 加载 NTUSD 中原有词语
    negative_words = set()
    positive_words = set()
    with open(negative_words_filename, 'r') as negative_file:
        for line in negative_file.readlines():
            negative_words.add(line.rstrip())
    with open(positive_words_filename, 'r') as positive_file:
        for line in positive_file.readlines():
            positive_words.add(line.rstrip())

    positive_file = open(positive_words_filename, 'a')
    negative_file = open(negative_words_filename, 'a')
    potential_file = open(potential_words_filename, 'r')
    for word in potential_file.readlines():
        negative = 0
        word = word.rstrip()
        print('与词语\"' + word + '\"最为相似的 8 个词语: ')
        similar_8_words = word2vec_model.wv.most_similar(word, topn=8)
        for item in similar_8_words:
            curr_word = item[0]
            print(curr_word, end='，')
            if curr_word in negative_words:
                negative += 1
            elif curr_word in positive_words:
                negative -= 1
        print()
        if negative == 0:
            print('无法判断\"' + word + '\"的极性')
        elif negative > 0:
            print('\"' + word + '\"为负面词语')
            negative_file.write(word + '\n')
        else:
            print('\"' + word + '\"为正面词语')
            positive_file.write(word + '\n')
    positive_file.close()
    negative_file.close()
    potential_file.close()


if __name__ == '__main__':
    potential_words_filename = 'potential_sentiment_words.txt'
    positive_words_filename = 'NTUSD_positive_simplified.txt'
    negative_words_filename = 'NTUSD_negative_simplified.txt'
    total_words_filename = 'NTUSD_words.txt'
    expand_sentiment_dict(potential_words_filename, positive_words_filename, negative_words_filename,
                          total_words_filename)
