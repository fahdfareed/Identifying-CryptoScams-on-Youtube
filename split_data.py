import csv
rows = []
with open("labels.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

train = rows[:6300]
test = rows[6301:]
with open('train.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in train:
        writer.writerow(i)

with open('test.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in test:
        writer.writerow(i)
