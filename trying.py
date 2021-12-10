import json


f = open('removed_duplicates_sorted_2.json')
data = json.load(f)

array = {}
for i in data["zeros"]:
    if i["scam"] == 0:
        for j in i["comment"].split(' '):
            j = j.lower()
            if j in array.keys():
                array[j] += 1
            else:
                array[j] = 1

f.close()
array = {k: v for k, v in sorted(array.items(), key=lambda item: item[1], reverse=False)}
print(array)

#with open('count.json', 'w') as outfile:
#    json.dump(array, outfile)
print(len(data["zeros"]), len(data["ones"]))