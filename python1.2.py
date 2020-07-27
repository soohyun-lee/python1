init = int(input('금액을 입력하세요'))

cost1 = init // 50000
init %= 50000

cost2 = init // 10000
init %= 10000

cost3 = init // 5000
init %= 5000

cost4 = init // 1000
init %= 1000

cost5 = init // 500
init %= 500

print('5만원은', cost1)
print('1만원은', cost2)
print('5천원은', cost3)
print('1천원은', cost4)
print('500원은', cost5)
print('그리고 나머지', init)