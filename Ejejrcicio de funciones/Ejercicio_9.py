def mcd(num1, num2):
    divisores1 = [x for x in range(1, num1+1) if num1%x == 0]
    divisores2 = [x for x in range(1, num2+1) if num2%x == 0]
    comunes = set(divisores1).intersection(divisores2)
    return max(comunes)

def mcm(a, b):
    return abs(a * b) // mcd(a, b)

print(mcd(24,36))
print(mcm(24,36))