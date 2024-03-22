# This Python code finds the largest prime factor of a given positive integer num.

def big_prime(num):
    divisor = []
    prime_divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    print("divisors : ", divisor)
    if is_prime(num) == True:
        return num
    else:
        for j in divisor:
            if is_prime(j) == True:
                prime_divisor.append(j)
        print("prime divisors : ", prime_divisor)
        return prime_divisor[-1]


def is_prime(num):
    for i in range(num):
        if num % i == 0:
            return True
    else:
        return False
      
