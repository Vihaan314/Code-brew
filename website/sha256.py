import struct

def sha256(data):
    # Initialize the hash values and message schedule
    h = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
    w = [0] * 64
    k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
         0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
         0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
         0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
         0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
         0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
         0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
         0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

    # Pre-processing
    padded_data = data + b'\x80' + (56 - len(data) % 64) * b'\x00' + struct.pack('>Q', 8 * len(data))
    data_len = len(padded_data)
    for i in range(0, data_len, 64):
        if i + 64 > data_len:
            remaining_data = padded_data[i:]
            remaining_len = len(remaining_data)
            padded_remaining_data = remaining_data + b'\x00' * (64 - remaining_len)
            for j in range(16):
                w[j] = struct.unpack('>I', padded_remaining_data[j * 4:j * 4 + 4])[0]
        else:
            for j in range(16):
                w[j] = struct.unpack('>I', padded_data[i + j * 4:i + j * 4 + 4])[0]
    # Initialize the working variables
    a, b, c, d, e, f, g, hh = h
    # Compression function
    for i in range(64):
        s0 = (a >> 2 | a << 30) ^ (a >> 13 | a << 19) ^ (a >> 22 | a << 10)
        maj = (a & b) ^ (a & c) ^ (b & c)
        t2 = s0 + maj
        s1 = (e >> 6 | e << 26) ^ (e >> 11 | e << 21) ^ (e >> 25 | e << 7)
        ch = (e & f) ^ ((~e) & g)
        t1 = hh + s1 + ch + k[i] + w[i]
        hh = g
        g = f
        f = e
        e = d + t1
        d = c
        c = b
        b = a
        a = t1 + t2
    # Add the compressed chunk to the current hash value
    for i, val in enumerate([a, b, c, d, e, f, g, hh]):
        h[i] += val
    # Produce the final hash value (big-endian)
    return bytes.fromhex(''.join(hex(val)[2:] for val in h))


data = "Hello"
data = data.encode()
print(sha256(data).hex())
