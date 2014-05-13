import itertools


code = tuple(int(c) for c in open('prob59_input.txt').read().split(','))

def decrypt(code, password):
    l = len(password)
    return tuple(c ^ password[i % l] for i, c in enumerate(code))

def text(code): return ''.join(chr(c) for c in code)



for password in itertools.permutations(tuple((ord(c) for c in list('abcdefghijklmnopqrstuvwxyz'))), 3):
    c = decrypt(code, password)
    t = text(c)
    if t.find(' the ') > 0:
        print sum(c)
        break
