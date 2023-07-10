def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
while True:
    try:
        num1=int(input())
        num2 =int(input())
        result = gcd(num1, num2)
        
    except EOFError:
        break