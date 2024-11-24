numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
primes = []
not_primes = []

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#         return True

def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a

# print(is_prime(int(input("Enter a number: "))))

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5)+1, 2):
#         if n % i == 0:
#             return False
#         return True

# def is_prime(a):
#     if a % 2 == 0:
#         return a == 2
#     d = 3
#     while d * d <= a and a % d != 0:
#         d += 2
#     return d * d > a

# for i in range(len(numbers)):
#     if is_prime(numbers[i]) and numbers[i] > 1:
#         primes.append(numbers[i])
#     elif numbers[i] > 1:
#         not_primes.append(numbers[i])
#
# print(f'Primes:',primes,'\nNot Primes:',not_primes)

# primes = []
# not_primes = []

for i in numbers:
    if is_prime(i) and i > 1:
        primes.append(i)
    elif i > 1:
        not_primes.append(i)

print(f'Primes:',primes,'\nNot Primes:',not_primes)
