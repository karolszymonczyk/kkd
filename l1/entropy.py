import sys
import os
from math import log2

if len(sys.argv) != 2:
    print("no filename provided")
    sys.exit()

filename = sys.argv[1]
f_size = os.stat(filename).st_size
freq = {}
freq_after = {}
entropy = 0
entropy_after = 0

with open(filename, "rb") as file:
    f_bytes = file.read()
    for i, b in enumerate(f_bytes):
        curr_tuple = (b, f_bytes[i - 1] if i > 0 else 0)
        if b not in freq:
            freq[b] = 0
        if curr_tuple not in freq_after:
            freq_after[curr_tuple] = 0
        freq[b] += 1
        freq_after[curr_tuple] += 1

for byte, amount in freq.items():
    entropy += (log2(f_size) - log2(amount)) * amount
    for t_byte, t_amount in freq_after.items():
        if t_byte[0] == byte:
            entropy_after += t_amount * (log2(amount) - log2(t_amount))

entropy /= f_size
entropy_after /= f_size

print(f"Filename: {filename}")
print(f"Entropy: {entropy}")
print(f"Entropy after elements: {entropy_after}")
print(f"Difference: {entropy - entropy_after}")
