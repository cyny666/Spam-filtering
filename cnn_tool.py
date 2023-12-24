import csv

def getlabel():
    cnn_classify_answer = []
    with open("cnn_mailclassify/runs/1703395381/prediction.csv", "r") as f:
        reader = csv.reader(f)

        for row in reader:
            if len(row) == 0:
                continue
            else:
                name = row[1]
                name = name.strip("b'").strip("'")
                name = float(name)
                name = int(name)
                cnn_classify_answer.append(name)
    return cnn_classify_answer

def csv2txt():
    with open('mail_content.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        content = ''
        for row in reader:
            content += ' '.join(row) + '\n'
    with open('mail_content.utf8', 'w', encoding='utf-8') as f:
        f.write(content)



