import json

f = open('removed_duplicates_sorted_2.json')
data = json.load(f)
count = 0
list = ["THESPACEHACKERS", "Vladimircorp", "vladimircorp", "COINSADDERCOM", "jasonmaddison2020", "ITECHHACKERSCOM",
    "Mrs. Patricia",
    "VIRTUALBTCINVESTCOM",
    "ELITECAPITAL",
    "REALSOURCEINVESTMENTORG",
    "REALSOURCEINVESTMENT",
    "VCORPINVEST",
    "ELITECAPITALLIMITED",
    "R e a l s o u r c e i n v e s t m e n t",
    "ELITECAPITAL",
    "mr",
    "mrwhosetheboss",
    "V I R T U A L B T C I N V E S T",
    "vladimir",
    "bullish.while",
    "----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "brian",
    "@brian",
    "ali",
    "xbritclonenet",
    "miss",
    "extremetopperscom",
    "coinsaddercom",
    "jayexpunge",
    "*jasonmaddison2020*",
    "worldsolutionhackercom",
    "detectifyhackcom",
    "*madrigal_kelvin_*",
    "expendablemoneysolutioncm",
    "$5000",
    "#topbrandwave",
    "maria",
    "topbrandwavecom",
    "eyeonsightnet",
    "#misttcyber",
    "q5cyber"
    "6btc",
    "$32000",
    "$4500",
    "#vladimircorp",
    "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "thespacehackerscom",
    "virtualbtcinvestcom",
    "#realsourceinvestment",
    "expendablemoneysolutioncom",
    "#vcorpinvest",
    "$",
    "Diana Brown",
    "instagram",
    "!g",
    "TRADERXTRACOM",
    "telegram", 
    "legit",
    "--------------------------------------------------------------------",
    "xbritclonenet",
    "mrs", 
    "shiba",
    "maya",
    "met",
    "net",
    "insta",
    "richard",
    "richardson",
    "richardson,",
    



    ]
zeros = []
nott = 0
for i in data["zeros"]:
    flag = 0
    for j in list:
        if j.lower() in i["comment"].lower():
            i["scam"] = 1
            data["ones"].append(i)
            count += 1
            flag = 1
            break
    if flag == 0:
        zeros.append(i)
        nott +=1
print(count)
print(nott)
data["zeros"] = zeros
print(len(data["ones"]))
f.close()
with open('removed_duplicates_sorted_2.json', 'w') as outfile:
    json.dump(data, outfile)
