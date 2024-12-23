#include <iostream>
#include <vector>

std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
std::vector<int> primes;
std::vector<int> not_primes;

bool is_prime(int a) {
    if (a % 2 == 0) {
        return a == 2;
    }
    int d = 3;
    while (d * d <= a && a % d != 0) {
        d += 2;
    }
    return d * d > a;
}

int main() {
    for (int i : numbers) {
        if (is_prime(i) && i > 1) {
            primes.push_back(i);
        } else if (i > 1) {
            not_primes.push_back(i);
        }
    }

    std::cout << "Primes: ";
    for (int p : primes) {
        std::cout << p << " ";
    }
    std::cout << "\nNot Primes: ";
    for (int np : not_primes) {
        std::cout << np << " ";
    }
    std::cout << std::endl;

    return 0;
}

