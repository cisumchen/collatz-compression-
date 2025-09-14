# Collatz Compression Operator

This repository implements and documents the **Compressed Collatz Operator**:

\[
T(n) = \frac{3n+1}{2^r}, \quad r = v_2(3n+1).
\]

where \(v_2(m)\) is the 2-adic valuation, i.e. the highest power of 2 dividing \(m\).

---

## What is this?

The classical Collatz map is:
- If \(n\) is even: \(n \mapsto n/2\)
- If \(n\) is odd: \(n \mapsto 3n+1\)

The compressed operator combines **one odd step** with all subsequent **even steps**, producing a shorter but equivalent trajectory.  
This allows us to analyze Collatz dynamics more clearly, with direct focus on the odd subsequence.

---

## Features

- **Compressed Collatz Operator** implementation in Python
- **Trajectory function**: generate compressed Collatz paths
- **Prime analysis**: track maximal and minimal primes along each path
- **Examples**: trajectory of n=41 (maximal prime 1619)

---

## Example (Python)

```python
def v2(m: int) -> int:
    r = 0
    while m % 2 == 0:
        m //= 2
        r += 1
    return r

def T(n: int) -> int:
    """Compressed Collatz operator (odd n only)."""
    if n % 2 == 0:
        raise ValueError("T(n) is defined only for odd n.")
    r = v2(3*n + 1)
    return (3*n + 1) // (2**r)

def trajectory(n0: int, max_steps: int = 1000) -> list[int]:
    seq = [n0]
    n = n0
    for _ in range(max_steps):
        if n == 1:
            break
        n = T(n)
        seq.append(n)
    return seq

print(trajectory(41))
## Related Preprint

For the full mathematical exposition, see the preprint:  
[Collatz Dynamics — Anchors and Prime Nodes (OSF Preprint)](https://osf.io/uv9zk/)
