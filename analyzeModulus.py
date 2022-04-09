def parseModulus(file):
  with open(file) as fp:
    for line in fp:
      if (line.startswith('Modulus=')):
        return line.replace('Modulus=', '')
  return Null

f = open('modulus.csv', 'w')
f.write('keyId,modulusSigBits,modulus\n')
for i in range(10000):
  filename = './keys/rsa-4096-{}.pub.modulus'.format(i + 1)
  modulus = parseModulus(filename)
  modulusDecimal = int(modulus, 16)
  modulusSigBits = bin(int(modulus[0:20], 16)).replace('0b', '')
  f.write('{},{},{}\n'.format(i + 1, modulusSigBits, modulusDecimal))
f.close()
