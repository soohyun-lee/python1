init = int(input('금액을 입력하세요'))
cost1 = init // 50000
init %= 50000
if cost1 > 0:
  print('5만원은', cost1)
cost2 = init // 10000
init %= 10000
if cost2 > 0:
  print('5만원은', cost2 )
cost3 = init // 5000
init %= 5000
if cost3 > 0:
  print('5천원은', cost3)
cost4 = init // 1000
init %= 1000
if cost4 > 0:
  print('천원은', cost4)
cost5 = init // 500
init %= 500
if cost5 > 0:
  print('오백원은', cost5)