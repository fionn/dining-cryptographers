#!/usr/bin/env python3
"""The dining cryptographers problem"""

from functools import reduce
from random import getrandbits
from dataclasses import dataclass


@dataclass
class Cryptographer:
    """A dining cryptographer"""
    position: int
    paid: bool = False
    left_secret_bit: bool = None
    right_secret_bit: bool = None

    def announce(self) -> bool:
        """Announce the result of the second stage computation"""
        return self.paid ^ self.left_secret_bit ^ self.right_secret_bit


def establish_shared_secret(left_cryptographer: Cryptographer,
                            right_cryptographer: Cryptographer) -> None:
    """Establish a shared secret between two cryptographers"""
    random_bit = bool(getrandbits(1))
    left_cryptographer.right_secret_bit = random_bit
    right_cryptographer.left_secret_bit = random_bit


def dining_cryptographers(n: int, payer_index: int) -> bool:
    """
    Generate n cryptographers and run through the protocol.
    Returns true if a cryptographer paid and false if NSA paid.
    """
    cryptographers = [Cryptographer(i) for i in range(n)]

    if 0 <= payer_index < n:
        cryptographers[payer_index].paid = True

    for i in range(n):
        establish_shared_secret(cryptographers[i],
                                cryptographers[(i + 1) % n])

    announcements = [c.announce() for c in cryptographers]
    return reduce(lambda a, b: a ^ b, announcements)


def main() -> None:
    """Entry point"""
    result = dining_cryptographers(5, 6)
    if result:
        print("Anonymous cryptographer paid")
    else:
        print("NSA paid")


if __name__ == "__main__":
    main()
