prime1BitsStats = [0] * 20
prime2BitsStats = [0] * 20

file = './primes-sigbits.csv'
with open(file) as fp:
  for line in fp:
    if (line.startswith('keyId')): continue

    (x, prime1, prime2) = line.split(',')
    for i in range(20): prime1BitsStats[i] = prime1BitsStats[i] + int(prime1[i])
    for i in range(20): prime2BitsStats[i] = prime2BitsStats[i] + int(prime2[i])

print(prime1BitsStats)
print(prime2BitsStats)

""""""

modulusBitsStats = [0] * 20

file = './modulus.csv'
with open(file) as fp:
  for line in fp:
    if (line.startswith('keyId')): continue

    (x, sigbits, modulus) = line.split(',')
    for i in range(20): modulusBitsStats[i] = modulusBitsStats[i] + int(sigbits[i])

print(modulusBitsStats)

"""
$ python3 bitsStats.py
[10000, 10000, 7507, 6266, 5615, 5280, 5099, 5070, 5082, 5074, 4972, 5028, 5074, 4891, 4963, 4979, 5012, 5029, 5020, 4986]
[10000, 10000, 2529, 3717, 4384, 4643, 4817, 4839, 4956, 4979, 4998, 5003, 4957, 4942, 4987, 5007, 4953, 4874, 5022, 5025]
[10000, 5448, 5339, 5009, 5068, 5004, 5028, 4985, 4987, 5062, 4986, 4934, 4956, 4994, 5042, 4951, 4971, 5053, 5061, 4933]
"""
