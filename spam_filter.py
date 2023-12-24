
from bayes_classify.main import classify_based_on_csv
from cnn_tool import csv2txt
from cnn_tool import getlabel
import os
from get_content.main import  get_content
import csv

def get_result():
    csv2txt()#把csv文件里的读成cnn方法需要的格式
    target = []
    # 朴素贝叶斯结果
    bayes_classify_answer = classify_based_on_csv(".\\mail_content.csv", ".\\bayes_classify\\ham.json", ".\\bayes_classify\\spam.json")
    print(bayes_classify_answer)
    # CNN 结果
    cnn_classify_answer = getlabel()
    print(cnn_classify_answer)
    for i in range(len(bayes_classify_answer)):
        if bayes_classify_answer[i] + cnn_classify_answer[i] == 2:
            target.append(i)
    return target
