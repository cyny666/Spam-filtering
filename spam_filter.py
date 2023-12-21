#from get_content.main import get_content
from bayes_classify.main import classify_based_on_csv
from cnn_tool import csv2txt
from cnn_tool import getlabel
import os

if __name__ == '__main__':
    # 获取邮件内容csv
    # get_content()

    csv2txt()#把csv文件里的读成cnn方法需要的格式

    # 朴素贝叶斯结果
    bayes_classify_answer = classify_based_on_csv(".\\mail_content.csv", ".\\bayes_classify\\ham.json", ".\\bayes_classify\\spam.json")
    print(bayes_classify_answer)

    # CNN 结果
    os.system('python ./cnn_mailclassify/eval.py')
    cnn_classify_answer = getlabel()
    print(cnn_classify_answer)
