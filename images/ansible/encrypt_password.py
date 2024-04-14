#!/usr/bin/env python
import sys
from passlib.hash import sha512_crypt


if len(sys.argv) < 2:
    print('Usage: ' + sys.argv[0] + '<password to encrypt>')
    sys.exit(1)

print(sha512_crypt.using(rounds=5000).hash(sys.argv[1]))
