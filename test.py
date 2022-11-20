#!/usr/bin/env python3
"""Test the dining cryptographers"""

import unittest

import dc

N = 5

class TestDiningCryptographers(unittest.TestCase):
    """Test the dining cryptographers problem"""

    def test_consistent_secrets(self) -> None:
        """Cryptographers agree on shared secrets"""
        cryptographers = [dc.Cryptographer(i) for i in range(N)]
        for i in range(N):
            dc.establish_shared_secret(cryptographers[i],
                                       cryptographers[(i + 1) % N])

        for i in range(N):
            self.assertEqual(cryptographers[i].right_secret_bit,
                             cryptographers[(i + 1) % N].left_secret_bit)

    def test_cryptographer_paid(self) -> None:
        """Anonymous cryptographer paid"""
        self.assertTrue(dc.dining_cryptographers(N, N - 1))

    def test_nsa_paid(self) -> None:
        """NSA paid"""
        self.assertFalse(dc.dining_cryptographers(N, N + 1))


if __name__ == "__main__":
    unittest.main(verbosity=2, buffer=True)
