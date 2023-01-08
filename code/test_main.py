import pandas as pd
import pytest
from .project import sieve_of_eratosthenes

def test_positives(prime, primes_obtained):
    assert prime in primes_obtained


def test_composites(composite, primes_obtained):
    assert composite not in primes_obtained


def test_negatives():
    with pytest.raises(ValueError):
        sieve_of_eratosthenes(-1)