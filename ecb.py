def hex_to_bin(hex_val):
    return bin(int(hex_val, 16))[2:].zfill(4)

def bin_to_hex(bin_val):
    return hex(int(bin_val, 2))[2:]

def shift_left(bin_val):
    return bin_val[1:] + bin_val[0]

def xor(bin_val, key):
    return ''.join('1' if b != k else '0' for b, k in zip(bin_val, key))

def ecb_encrypt(plaintext, key):
    plaintext = [hex_to_bin(c) for c in plaintext]
    key = key.zfill(4)
    ciphertext = []
    for block in plaintext:
        xor_result = xor(block, key)
        shifted = shift_left(xor_result)
        ciphertext.append(bin_to_hex(shifted))
    return ciphertext

# Ganti dengan nama dan nim Anda
print("Nama: Yusuf Putra Bintang Satria")
print("NIM: 312110317")
print("Kelas: TI.21.A.2")

plaintext = input("Masukkan Plainteks :")
key = input("Masukkan kunci :")
ciphertext = ecb_encrypt(plaintext, key)
print("Hasil enkripsi ecb:", ciphertext)