import tangram
import csv


f = open('test.csv')
data = csv.reader(f)
rows = []
for row in data:
    rows.append(row)
f.close()

model = tangram.Model.from_path('../../../go/scam3.tangram')
t_p = 0
t_n = 0
f_p = 0
f_n = 0
for i in rows:
    output = model.predict({"comment": i[0]})
    if i[1] == "1" and output.class_name == "1":
        t_p += 1
    if i[1] == "1" and output.class_name == "0":
        f_n += 1
    if i[1] == "0" and output.class_name == "0":
        t_n += 1
    if i[1] == "0" and output.class_name == "1":
        f_p += 1
    
print("tp: ", t_p, "tn: ", t_n, "fp: ", f_p, "fn: ", f_n)

