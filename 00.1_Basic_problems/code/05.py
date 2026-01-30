def gretest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

print(gretest_common_divisor(18, 36))



def gcd(a, b):
    ans = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            ans = i
    return ans

print(gcd(100, 30))

# dry run
# step 1 : a = 100, b = 30  =  b = 30 , a = 100 % 30 = 10
# step 2 : a = 30, b = 10  =  b = 10 , a = 30 % 10 = 0
# step 3 : a = 10, b = 0  =  return a