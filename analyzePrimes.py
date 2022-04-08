def hexToDecimal(primeInHex):
  hex = primeInHex.strip().replace('\n', '').replace(' ', '').replace(':', '')
  dec = int(hex, 16)
  return dec

def parsePrimes(file):
  isPrime1 = False
  isPrime2 = False
  prime1 = ''
  prime2 = ''
  with open(file) as fp:
    for line in fp:
      if (line.startswith('prime1')):
        isPrime1 = True
        continue
      if (line.startswith('prime2')):
        isPrime2 = True
        continue
      if (line.startswith('exponent1')):
        break

      if (isPrime2):
        prime2 = prime2 + line
      elif (isPrime1):
        prime1 = prime1 + line
  return (prime1, prime2)

def getSignificantBits(prime, numBits):
  return prime

f = open('primes.csv', 'w')
f2 = open('primes-sigbits.csv', 'w')
f.write('keyId,prime1,prime2\n')
f2.write('keyId,prime1,prime2\n')
for i in range(10000):
  filename = './keys/rsa-4096-{}.pem.modulus'.format(i + 1)
  primes = parsePrimes(filename)
  prime1Decimal = hexToDecimal(primes[0])
  prime2Decimal = hexToDecimal(primes[1])
  prime1SigBinary = bin(hexToDecimal(primes[0][0:20])).replace('0b', '')
  prime2SigBinary = bin(hexToDecimal(primes[1][0:20])).replace('0b', '')
  f.write('{},{},{}\n'.format(i + 1, prime1Decimal, prime2Decimal))
  f2.write('{},{},{}\n'.format(i + 1, prime1SigBinary, prime2SigBinary))
f.close()
