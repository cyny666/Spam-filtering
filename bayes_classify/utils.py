import re
import math


def keep_chinese_and_english(input_string):
    # 使用正则表达式匹配汉字和英文字母
    pattern = re.compile("[^\u4e00-\u9fa5a-zA-Z]")
    result_string = pattern.sub("", input_string)
    return result_string


def laplacian_smoothing_probability(class_instance_number, class_instance_with_feature_number):
    lambda_c = 1.00
    s_j = 2.00

    probability = float((class_instance_with_feature_number + lambda_c) / (class_instance_number + s_j * lambda_c))
    return probability
