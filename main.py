import string

alphabet = list(string.ascii_lowercase)
nums = list(range(1,27))

alphanum = dict(zip(alphabet, nums))

lookup = []
cipher_shifted = []
ciphertext = []
secret = 0

print("All non-alpha characters are stripped, translated to lowercase")
print("i.e. 'Hello, world!' -> helloworld")
print("Note that for k values, 25 results in no shifting")
print("To reverse, use -/+ (abs(k) +/- 2 ) (k.ispos, k.isneg)")
print("i.e. k == 4 --> k.rev == -6")

plaintext = input("Plaintext: ").lower()
for c in plaintext:
    if not c.isalpha():
      plaintext = plaintext.replace(c, '')
while not secret:
    try:
      secret = int(input("k: "))
    except ValueError:
      print("Please enter an integer in range 1-26")
for c in plaintext:
    lookup.append(alphanum[c])
for c in lookup:
    # + 1 needed to ensure that the index doesn't include 0s
    cipher_shifted.append((c + secret) % len(alphabet) + 1)
for c in cipher_shifted:
    ciphertext.append(list(alphanum.keys())[list(alphanum.values()).index(c)])
print(''.join(ciphertext))
