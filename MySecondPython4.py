print("2017112197 이승훈")
data_type = ['str', 'int', 'float', 'complex', 'list', 'tuple', 'dict', 'set']
print(data_type)

for x in data_type:
    if x =="complex":
        continue
    if x == "dict":
        break
    print(x)