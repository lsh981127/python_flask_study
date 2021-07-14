class Person:
    def __init__(mysillyobject, name, age):    ''' mysillyobject가 self parameter 인거임. 무조건 제일 첫번째 매개변수로 작성! '''
        mysillyobject.name = name               
        mysillyobject.age = age

    def myfunc(abc):    #abc 도 self parameter
        print("Hello my name is " + abc.name)

p1 = Person("Jiyoung", 24)
p1.myfunc()