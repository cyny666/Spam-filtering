from get_content.main import get_content
from bayes_classify.main import classify_based_on_csv
from cnn_mailclassify.eval import eval

if __name__ == '__main__':
    # 获取邮件内容csv
    # get_content()

    # 朴素贝叶斯结果
    bayes_classify_answer = classify_based_on_csv(".\\mail_content.csv", ".\\bayes_classify\\ham.json", ".\\bayes_classify\\spam.json")
    print(bayes_classify_answer)

    # CNN 结果
    eval()