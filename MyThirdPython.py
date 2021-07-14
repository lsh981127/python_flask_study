print("2017112197 이승훈")
def func(*args, **kwargs):   #*변수 => 전달 될 인수의 수를 모를떄, **변수 => 키워드 인수의 수를 모르는경우
    for x in args:
        print(x)
    print('My name : ', kwargs["name"], ' & My age : ', kwargs["age"])

func(1,2,3,4, name='SeongHoon', age=24) 