def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
a = int(input())
b = int(input())
lcm_result = lcm(a, b)
print(lcm_result)