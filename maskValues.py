modulusBitsStats = [0] * 256

file = './modulus.csv'
with open(file) as fp:
  for line in fp:
    if (line.startswith('keyId')): continue

    (x, sigbits, modulus) = line.split(',')
    a = int('0b' + sigbits[1:9], 2)
    modulusBitsStats[a] = modulusBitsStats[a] + 1

print(modulusBitsStats)

"""
$ python3 maskValues.py
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 8, 0, 3, 6, 2, 9, 9, 8, 6, 15, 18, 16, 22, 4, 19, 17, 19, 14, 15, 21, 28, 26, 26, 32, 28, 42, 41, 26, 32, 40, 33, 30, 37, 35, 38, 45, 30, 36, 35, 37, 33, 45, 37, 40, 59, 47, 60, 42, 52, 63, 55, 63, 54, 40, 51, 53, 70, 66, 63, 54, 43, 72, 61, 54, 63, 70, 68, 64, 70, 59, 49, 64, 79, 66, 82, 74, 65, 78, 71, 88, 87, 79, 78, 81, 100, 86, 96, 86, 98, 88, 94, 91, 92, 96, 96, 86, 91, 93, 82, 84, 87, 74, 78, 73, 60, 90, 88, 79, 73, 75, 76, 76, 66, 69, 80, 72, 63, 81, 80, 67, 62, 58, 58, 64, 70, 68, 69, 70, 50, 58, 58, 64, 64, 68, 67, 48, 56, 53, 53, 61, 59, 63, 40, 44, 59, 50, 45, 54, 45, 38, 52, 43, 53, 40, 50, 36, 43, 32, 47, 50, 48, 37, 40, 39, 48, 38, 35, 46, 33, 36, 38, 39, 23, 32, 28, 32, 28, 25, 30, 32, 18, 34, 28, 23, 33, 26, 20, 29, 22, 17, 14, 19, 17, 15, 32, 16, 14, 13, 10, 10, 7, 11, 9, 11, 10, 11, 10, 10, 2, 8, 1, 9, 2, 4, 6, 8, 5, 3, 1, 1, 1, 0]
"""