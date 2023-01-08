import pandas as pd
import pytest

from .project import sieve_of_eratosthenes


def pytest_addoption(parser):
    parser.addoption(
        "--primes",
        action="store",
        default='100',
        help="Upper bound for primes to test."
    )
    parser.addoption(
        "--composites",
        action="store",
        default='100',
        help="Upper bound for composites to test."
    )


def pytest_configure(config):
    pytest.primes = int(config.getoption("--primes"))
    pytest.composites = int(config.getoption("--composites"))


def pytest_generate_tests(metafunc):
    df_prime = pd.read_csv("P-100000.csv", header=None)
    df_prime = df_prime[df_prime.iloc[:, 1] <  pytest.primes]
    primes = set(df_prime.iloc[:, 1])
    df_composite = pd.read_csv("C-100000.csv", header=None, delimiter="=")
    # interpret first oclumns as numbers
    df_composite = df_composite[df_composite.iloc[:, 0] < pytest.composites]
    composites = set(df_composite.iloc[:, 0])
    if metafunc.function.__name__ == 'test_positives':
        metafunc.parametrize('prime', primes)
        metafunc.parametrize('primes_obtained', [sieve_of_eratosthenes(max(primes) + 1),])

    if metafunc.function.__name__ == 'test_composites':
        metafunc.parametrize('composite', composites)
        metafunc.parametrize('primes_obtained', [sieve_of_eratosthenes(max(composites) + 1),])
