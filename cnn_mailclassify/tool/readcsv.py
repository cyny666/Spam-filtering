import csv
with open('prediction.csv') as file:
    csv_file = csv.reader(file)
    for row in csv_file:
        print(row)
