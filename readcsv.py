import csv
with open('mail_content.csv',encoding='utf-8') as file:
    csv_file = csv.reader(file)
    for row in csv_file:
        print(row)
