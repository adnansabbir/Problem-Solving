# We need to proof is this statement is wrong for 1<n<1000000

def isPrime(n):
    # Corner case
    if (n <= 1):
        return False

    # Check from 2 to n-1
    for i in range(2, n):
        if (n % i == 0):
            return False

    return True


for i in range(2, 1000000):
    if not isPrime(i * (i + 1) + 41):
        print(i)
