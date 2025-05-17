# -*- coding: utf-8 -*-

my_sum = 0
for i in range(5, 11, 2):
    my_sum += i
    if my_sum == 5:
        break
        my_sum += 1 # nunca vai ser executado, pois está após um break.
print(my_sum) # 5
