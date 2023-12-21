import os
import json
import math
import random
import csv

import jieba

from bayes_classify.utils import keep_chinese_and_english, laplacian_smoothing_probability


def read_csv(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        csvreader = csv.reader(f)
        final_list = list(csvreader)
    return final_list


def email_analysis(file_path_list, words_limit=5000, save=False, output=None):
    """统计邮件词频"""
    # 获取文件列表
    file_name_list_cnt = len(file_path_list)

    word_freq_dict = {}  # 词频字典
    cnt = 1
    for file_path in file_path_list:

        # 读取文件内容
        with open(file_path, 'r', encoding='UTF-8') as file:
            file_content = file.read()

        # 去除标点符号
        file_content = keep_chinese_and_english(file_content)
        # 分割词组
        word_seq_list = jieba.cut(file_content, cut_all=True)

        # 统计词频
        for word in word_seq_list:
            # 删除单字词
            if len(word) < 2:
                continue
            if word not in word_freq_dict:
                word_freq_dict[word] = 0
            else:
                word_freq_dict[word] += 1

        if cnt % 1000 == 0:
            print("Finished counting job: {}/{}".format(cnt, file_name_list_cnt))
        # 开启下轮循环
        cnt += 1

    # 按值的大小由大到小排序字典
    sorted_word_freq_dict = dict(sorted(word_freq_dict.items(), key=lambda item: item[1], reverse=True))

    # 输出统计信息
    limit_cnt = 0
    final_words_freq = {}
    for word, distribution in sorted_word_freq_dict.items():
        # 限制打印数量
        if limit_cnt == words_limit:
            break
        # 加入最终字典中
        final_words_freq[word] = {
            'distribution': distribution,
            'total': file_name_list_cnt
        }
        limit_cnt += 1

    # 保存
    if save:
        if output is not None:
            with open(output + '.json', 'w', encoding='utf-8') as json_file:
                json.dump(final_words_freq, json_file, ensure_ascii=False)

    return final_words_freq


def get_word_dict(ham_file_path_list, spam_file_path_list, words_limit=5000, replace=True):
    if replace:
        print("begin to analyze the training set again...")
        ham_word_dict = email_analysis(ham_file_path_list, words_limit=words_limit, save=True, output='ham')
        spam_word_dict = email_analysis(spam_file_path_list, words_limit=words_limit, save=True, output='spam')
    else:
        with open('ham.json', 'r', encoding='utf-8') as json_file:
            ham_word_dict = json.load(json_file)
        with open('spam.json', 'r', encoding='utf-8') as json_file:
            spam_word_dict = json.load(json_file)
    return ham_word_dict, spam_word_dict


def classify(content, ham_word_dict, spam_word_dict):
    # 去除标点符号
    content = keep_chinese_and_english(content)
    # 分割词组
    words_list = jieba.cut(content, cut_all=True)
    # 计算中间值
    ham_prob = math.log(16556.0 / (16556 + 27360), 10)
    spam_prob = math.log(27360.0 / (16556 + 27360), 10)

    # 开始计算
    for word in words_list:
        ham_number = ham_word_dict[word]["distribution"] if word in ham_word_dict else 0
        spam_number = spam_word_dict[word]['distribution'] if word in spam_word_dict else 0
        ham_prob += math.log(laplacian_smoothing_probability(16556, ham_number))
        spam_prob += math.log(laplacian_smoothing_probability(27360, spam_number))

    return ham_prob, spam_prob


def test():
    spam_directory = 'D:\\AppData\\WeChat\\WeChat Files\\wxid_v8q3aeroqkoa22\\FileStorage\\File\\2023-12\\spam_all\\spam_all\\'
    ham_directory = 'D:\\AppData\\WeChat\\WeChat Files\\wxid_v8q3aeroqkoa22\\FileStorage\\File\\2023-12\\ham_all\\ham_all\\'
    spam_list = os.listdir(spam_directory)
    ham_list = os.listdir(ham_directory)
    spam_training_list = []
    spam_testing_list = []
    ham_training_list = []
    ham_testing_list = []

    # 构建训练集
    for i in range(10000):
        rd = random.randint(1, len(spam_list))
        spam_training_list.append(spam_directory + spam_list[rd - 1])
        del spam_list[rd - 1]

    for i in range(10000):
        rd = random.randint(1, len(ham_list))
        ham_training_list.append(ham_directory + ham_list[rd - 1])
        del ham_list[rd - 1]

    print("Finish generating training files, begin to train")

    ham_word_dict, spam_word_dict = get_word_dict(ham_training_list, spam_training_list, words_limit=20000,
                                                  replace=True)

    print("Finish training, begin to test")

    # 构建测试集
    for i in range(500):
        rd = random.randint(1, len(spam_list))
        spam_testing_list.append(spam_directory + spam_list[rd - 1])
        del spam_list[rd - 1]

    for i in range(1000):
        rd = random.randint(1, len(ham_list))
        ham_testing_list.append(ham_directory + ham_list[rd - 1])
        del ham_list[rd - 1]

    print("Finish generating testing files, begin to test.")

    # testing spam
    spam_cnt = 0
    ham_cnt = 0

    cnt = 0
    for file in spam_testing_list:
        cnt += 1
        if cnt % 1000 == 0:
            print("Testing: {} / {}".format(cnt, len(spam_testing_list)))
        with open(file, 'r', encoding='UTF-8') as f:
            content = f.read()
        ham_prob, spam_prob = classify(content, ham_word_dict, spam_word_dict)
        if ham_prob > spam_prob:
            ham_cnt += 1
        else:
            spam_cnt += 1

    spam_accuracy = float(spam_cnt) / len(spam_testing_list)

    # testing ham
    spam_cnt = 0
    ham_cnt = 0

    cnt = 0
    for file in ham_testing_list:
        cnt += 1
        if cnt % 1000 == 0:
            print("Testing: {} / {}".format(cnt, len(ham_testing_list)))
        with open(file, 'r', encoding='UTF-8') as f:
            content = f.read()
        ham_prob, spam_prob = classify(content, ham_word_dict, spam_word_dict)
        if ham_prob > spam_prob:
            ham_cnt += 1
        else:
            spam_cnt += 1

    ham_accuracy = float(ham_cnt) / len(ham_testing_list)

    print("Ham accuracy: {}; Spam accuracy: {}".format(ham_accuracy, spam_accuracy))


def classify_based_on_csv(csv_file_path, ham_word_dict_path, spam_word_dict_path):
    data_list = read_csv(csv_file_path)
    del data_list[0]
    content_list = []

    for data in data_list:
        content_list.append(data[3])
    print(content_list)

    # 读取关键字文件
    with open(ham_word_dict_path, 'r', encoding='utf-8') as json_file:
        ham_word_dict = json.load(json_file)
    with open(spam_word_dict_path, 'r', encoding='utf-8') as json_file:
        spam_word_dict = json.load(json_file)

    answer_list = []
    for content in content_list:
        ham_prob, spam_prob = classify(content, ham_word_dict, spam_word_dict)
        answer_list.append(1 if ham_prob > spam_prob else 0)

    return answer_list



