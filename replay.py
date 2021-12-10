import json

f = open('removed_duplicates_sorted_2.json')
data = json.load(f)

f.close()
ones = []

for i in data["ones"]:
    if "ali" in i["comment"]:
        i["scam"] = 1
        ones.append(i)
    else:
        ones.append(i)

data["ones"] = ones
with open('removed_duplicates_sorted_2.json', 'w') as outfile:
    json.dump(data, outfile)


