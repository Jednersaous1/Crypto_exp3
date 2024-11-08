#Euler182

def gcd(a,b):
    if a > b:
        t = a
        a = b
        b = a
    while a > 0:
        t = a
        a = b % a
        b = t
    return b

p = 1009
q = 3643
n = p * q
fai = (p - 1) * (q - 1)

#暴力求解失败
# for e in range(2,fai):
#     if gcd(e, fai) == 1:
#         count = 0
#         for m in range(0,n):
#             if pow(m, e, n) == m:
#                 count = count + 1
#         if count > max:
#             max = count
# print(max)

# 计算模逆元
inv_p = pow(p, -1, q)
inv_q = pow(q, -1, p)

# 寻找最小的不动点数目
min_count = float('inf')
min_es = []

for e in range(2, fai):
    if gcd(e, fai) == 1:
        # 计算不动点的数量
        count = (p - 1) * (q - 1) // gcd(e - 1, p - 1) // gcd(e - 1, q - 1)
        
        # 更新最小不动点数目
        if count < min_count:
            min_count = count
            min_es = [e]
        elif count == min_count:
            min_es.append(e)

result = sum(min_es)
print("Result:", result)