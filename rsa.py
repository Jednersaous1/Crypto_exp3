import random
import binascii

# GCD function
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Extended Euclidean Algorithm (for modular inverse)
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def invmod(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError('Modular inverse does not exist')
    else:
        return x % m

# Function to generate a random prime number (simple approach)
def generate_prime_candidate(length):
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1  # Ensure the number is odd and has the correct length
    return p

# Simple primality test (Miller-Rabin is better for large primes)
def is_prime(n, k=128):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Generate a prime number of a given bit length
def generate_prime_number(length=1024):
    p = 4
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p

# Generate two random primes p and q
p = generate_prime_number(512)
q = generate_prime_number(512)

# Calculate n and totient (et)
n = p * q
et = (p - 1) * (q - 1)

# Set the public exponent e, we will ensure it is coprime with et
e = 3
while gcd(e, et) != 1:  # Keep trying different values for e until it works
    e += 2  # Increment by 2 to ensure it's always odd (since even numbers aren't coprime with et)

# Calculate private exponent d (modular inverse of e mod et)
d = invmod(e, et)

# Public and private keys
public_key = (e, n)
private_key = (d, n)

print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")

# Encrypt and decrypt a number (e.g., 42)
m = 42
c = pow(m, e, n)
decrypted_m = pow(c, d, n)
print(f"Original message: {m}")
print(f"Encrypted message: {c}")
print(f"Decrypted message: {decrypted_m}")

# Encrypt and decrypt a string
message = "Hello, RSA!"
m = int(binascii.hexlify(message.encode()), 16)
c = pow(m, e, n)
decrypted_m = pow(c, d, n)
decrypted_message = binascii.unhexlify(hex(decrypted_m)[2:]).decode()

print(f"Original string message: {message}")
print(f"Encrypted message as number: {c}")
print(f"Decrypted string message: {decrypted_message}")
print(e)