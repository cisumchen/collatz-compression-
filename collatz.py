def v2(m: int) -> int:
    """Return the 2-adic valuation v2(m)."""
    r = 0
    while m % 2 == 0:
        m //= 2
        r += 1
    return r

def T(n: int) -> int:
    """Compressed Collatz operator on odd n."""
    if n % 2 == 0:
        raise ValueError("T(n) is defined only for odd n.")
    r = v2(3*n + 1)
    return (3*n + 1) // (2**r)

def trajectory(n0: int, max_steps: int = 1000) -> list[int]:
    """Compute compressed Collatz trajectory starting from odd n0."""
    if n0 % 2 == 0:
        raise ValueError("Trajectory starts with odd n0.")
    seq = [n0]
    n = n0
    for _ in range(max_steps):
        if n == 1:
            break
        n = T(n)
        seq.append(n)
    return seq

if __name__ == "__main__":
    print("Trajectory of 41:")
    print(trajectory(41))
  
