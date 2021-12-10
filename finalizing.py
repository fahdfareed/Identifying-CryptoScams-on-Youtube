import json
import random
import csv

f = open('removed_duplicates_sorted_2.json')
data = json.load(f)

zeros = []
for i in data["zeros"]:
    if i["scam"] == 1:
        data["ones"].append(i)
    else:
        zeros.append(i)

print(len(zeros))
data["zeros"] = zeros

data["final"] = data["ones"]
for i in data["zeros"]:
    data["final"].append(i)

random.shuffle(data["final"])

final = data["final"]
with open('labels.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(['comment', 'label'])
    for i in final:
        row = [i["comment"].replace(',', ''), i["scam"]]
        writer.writerow(row)

f.close()