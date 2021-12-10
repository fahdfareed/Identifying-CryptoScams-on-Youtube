import json
import os
import re

ids = ["JgEcBdiadms",
    "mQvw5JXXnrQ",
    "rYQgy8QDEBI",
    "gFQNPmLKj1k",
    "Yb6825iv0Vk",
    "WFQRXDqLUHY",
    "atvJwwec_2A"
    ]

comments = [] 

for i in ids:
    path = os.getcwd() + '/data/youtube_videos/comments/' + i + '.json'
    f = open(path)
    data = json.load(f)
    for j in data:
        text = j["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
        text.replace('\n', ' ')
        comments.append({"etag": j["etag"], "comment": re.sub(r'[^\x00-\x7f]',r'',text), "scam":0})
        try:
            for k in j["replies"]["comments"]:
                text = k["snippet"]["textOriginal"]
                text.replace(b'\n', ' ')
                comments.append({"etag": k["etag"], "comment": re.sub(r'[^\x00-\x7f]',r'',text), "scam": 0})
        except:
            pass
    
    f.close()

with open('all_comments.json', 'w') as outfile:
    json.dump(comments, outfile)