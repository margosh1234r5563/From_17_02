k_result, a_result, s_result = map(int, input().split())
if k_result > a_result and k_result > s_result:
    print(k_result)
elif a_result > k_result and a_result > s_result:
    print(a_result)
elif s_result > a_result and s_result > k_result:
    print(s_result)
else:
    print('Победила дружба')
