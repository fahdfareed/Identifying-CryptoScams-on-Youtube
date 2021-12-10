import json

f = open('all_comments.json')
data = json.load(f)
array = []
no_duplicate = []
for i in data:
    if i["comment"] not in array:
        array.append(i["comment"])
        no_duplicate.append(i)
    else:
        i["scam"] = 1
        no_duplicate.append(i)
        

f.close()
array = []
new_no_duplicate = []
for i in no_duplicate[::-1]:
    if i["comment"] not in array:
        array.append(i["comment"])
        new_no_duplicate.append(i)

with open('removed_duplicates.json', 'w') as outfile:
    json.dump(new_no_duplicate, outfile)
