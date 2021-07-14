def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("\n\n재귀 예시의 결과")
tri_recursion(6)        