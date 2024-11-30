# list_ = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numbers = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
primes = []
not_primes = []

def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a

for i in numbers:
    string = ''
    if is_prime(i): #3 - 12
        for j in range(int(i)-1, 1, -1):
            x = i - j
            if x < j:
                print(i,x,j, '1')
        #         string += str(x) + str(j)
        # print(i,string)
    else:
        for j in range(1, int(i), 1):
            if i % j == 0:
                for k in range(1, int(i/2), 1):
                    x = j -k
                    y = j - 1
                    if x < y:
                        print(i, x, y, '2')
                        # string += str(x) + str(y)
            else:
                # for j in range(int(i) - 1, 1, -1):
                x = i - j
                if x < j:
                    print(i, x, j, '3')
        #             string += str(x) + str(j)
        # print(i, string)

# print(f'Primes:',primes,'\nNot Primes:',not_primes)

# for i in range(len(list_)):
#     for j in range(1, int(list_[i]/2)):
#         x = list_[i] - j
#         print(x, i, j)