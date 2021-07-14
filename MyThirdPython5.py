print("2017112197 이승훈")
import json

x = {
    "name" : "SeongHoon",
    "age" : 24,
    "attending" : True,
    "discharge" : True,
    "phones" : [
        {"model" : "iphone 11 pro", "year" : 2019},
        {"model" : "galaxy s20", "year" : 2020}
    ]
}       #dict형태

print('json.dumps(x)')
print(json.dumps(x))
print('\njson.dumps(x, indent=4)')       #indent는 들여쓰기의 수 정의
print(json.dumps(x, indent =4))
print('\njson.dumps(x, indent = 4, separators=(". ", " = "))')    #separators 구분 기호
print(json.dumps(x, indent = 4, separators=(". ", " = ")))
print('\njson.dumps(x, indent = 4, sort_keys=True)')     #결과 정렬해야하는지 여부 지장
print(json.dumps(x, indent = 4, sort_keys=True))