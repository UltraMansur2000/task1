nums = []
Sum = 0
Sum1 = 0
for i in range(1, 1001, 2):
    s = 0
    nums.append(i ** 3)
    num = str(i ** 3)
    for i in num:
        s += int(i)
    if s % 7 == 0:
        Sum += int(num)

for i in range(len(nums)):
    s = 0
    nums[i] += 17
    for l in str(nums[i]):
        s += int(l)
    if s % 7 == 0:
        Sum1 += nums[i]
print(f'Контрольная сумма для первого условия:{Sum} \nКонтрольная сумма для второго условия:{Sum1}')
