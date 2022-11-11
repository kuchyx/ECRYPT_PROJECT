'''Python program to print all Primes Smaller than or equal to N using Sieve of Eratosthenes'''
import time
import math
  
def sieve_of_eratosthenes(num: int) -> list[int]:
    """Finds all prime number from 1 to num.
    
    Args:
        num (int): Number up to which the prime numbers should be printed
    
    Returns:
        list[int]: List of prime numbers
    """
    # boolean list
    prime = [True] * (num+1)
    p = 2
    while p <= math.sqrt(num):
        # If prime[p] is not
        # changed, then it is a prime
        if prime[p]:
            i = (p << 1)
            # Updating all multiples of p
            while i <= num:
                prime[i] = False
                i += p
        p += 1
    return [p for p in range(2, num+1) if prime[p]]


def print_sieve(num: int) -> None:
    """Prints all prime number from 1 to num.

    Args:
        num (int): Number up to which the prime numbers should be printed
    """
    for number in sieve_of_eratosthenes(num):
        print(number, end=" ")
  
  
# Driver code
if __name__ == '__main__':
    num = 3000
    print("Following are the prime numbers smaller"),
    print("than or equal to", num)
    print_sieve(num)