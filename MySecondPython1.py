fruitlist = ["banana", "Orange", "Kiwi", "cherry"]
print("2017112197 이승훈")
print('Original list : ', fruitlist)

fruitlist.reverse()             #역으로 정렬
print('reverse() -> ', fruitlist)

fruitlist.sort()            #대소문자 구분해서 정렬
print('sort() -> ', fruitlist)

fruitlist.sort(key=str.lower)       #대소문자 구분안하고 알파벳 순서로 정렬(key=str.lower)
print("sort(key=str.lower) -> ", fruitlist)