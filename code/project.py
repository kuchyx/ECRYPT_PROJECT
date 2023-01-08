'''Python program to print all Primes Smaller than or equal to N using Sieve of Eratosthenes'''
import math
  
def sieve_of_eratosthenes(num: int) -> list[int]:
    """Finds all prime number from 1 to num.
    
    Args:
        num (int): Number up to which the prime numbers should be printed
    
    Returns:
        list[int]: List of prime numbers
    """
    if num <= 0:
        raise ValueError("Number should not be negative.")
    # boolean list to store if a number is prime or not
    prime = [True] * (num+1)
    p = 2 # starting prime number
    # we will iterate till square root of num because 
    # if a number is not prime then it will have a factor less than or equal to square root of that number
    while p <= math.sqrt(num):
        # If prime[p] is not
        # changed, then it is a prime
        if prime[p]:
            i = (p << 1) # i = p * 2
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
    num = int(input("Enter a number: "))
    print(f"Following are the prime numbers smaller than or equal to {num}")
    print_sieve(num)