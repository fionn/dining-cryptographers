# Dining Cryptographers Problem

Secure multiparty computation of single bit xor.

This simulates the protocol described in [`doi:10.1007/BF00206326`](https://doi.org/10.1007/BF00206326).

## Usage

### As a Command

Execute `./dc.py` to run a simulation with a fixed number and payer.

### As a Library

Instantiate a `Cryptographer` with no arguments. By default, `Cryptographer.paid` is false.

Establish a shared secret between adjacent cryptographers with `establish_shared_secret`, which takes two cryptographers as arguments.

Cryptographers have the `announce` method which takes no arguments and returns a boolean as the result of the second stage computation from the paper.

We can run through the whole protocol with `dining_cryptographers(n: int, payer_index: int) -> bool`, where `n` is the number of cryptographers and `payer_index` is the index of the payer, which may greater than or equal to `n`.
