import pandas as pd

def test_positives(prime, primes_obtained):
    assert prime in primes_obtained


def test_negatives(composite, primes_obtained):
    assert composite not in primes_obtained