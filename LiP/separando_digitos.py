number = int(input())

d_m = number // 10000
u_m = (number % 10000) // 1000
c = ((number % 10000) % 1000 )// 100
d = (((number % 10000) % 1000) % 100) // 10
u = (((number % 10000) % 1000) % 100) % 10

print(f"{d_m}   {u_m}   {c}   {d}   {u}")