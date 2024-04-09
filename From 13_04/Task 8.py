result = 8
srt = '1'
for i in range(1, 10):
    print(srt, '*', result, '+', i, '=', result * int(srt) + i)
    srt += str(i + 1)
print()
result = 9
srt = '1'
for i in range(2, 11):
    print(srt, '*', result, '+', i, '=', result * int(srt) + i)
    srt += str(i)

result = '1'
srt = '1'
for i in range(2, 11):
    print(srt, '*', result, '=', int(result) * int(srt))
    srt += str(1)
    result += str(1)
