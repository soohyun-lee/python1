# 홀수 = x, 짝수 = y
number = list(range(1,31))
x = sum(number[::2])
y = sum(number[1::2])
print(x)
print(y)

====================================================================
# for

even = 0
odd = 0

for i in range(1,31):
  if i % 2 == 0:
    even += i
  else:
    odd += i
print(odd)
print(even)